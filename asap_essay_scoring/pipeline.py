'''
A collection of wrappers for other asap_essay_scoring functions to support
operating each function using file(s) input and writing the output to file(s)

These functions make lots of assumptions about the format and contents of input files.
It could make sense to break off this submodule from the main module if asap_essay_scoring
develops into a more general tool (not specific to ASAP-AES)
'''
from gensim.models.word2vec import Word2Vec
import pandas as pd

from . import conf
from . import tokens
from . import utils
from . import vocab

def tokenize(infile, outfile):
    df = pd.read_csv(infile, sep='\t', encoding="ISO-8859-1")
    tk = tokens.Tokenizer()
    doc_list = tk.apply_tokenize(df.essay)
    utils.json_save(doc_list, outfile)

def reduce_docs_to_smaller_vocab(infile, outfile):
    doc_list = utils.json_load(infile)
    vc = vocab.Vocab(vocab_size=3000)
    vc.build_from_tokenized_docs(doc_list)
    reduced_docs = vc.reduce_docs(doc_list)
    utils.json_save(reduced_docs, outfile)

def fit_word2vec(infile, outfile):
    reduced_docs = utils.json_load(infile)
    wv = Word2Vec(reduced_docs, size = 25, iter = 25)
    wvdf = pd.DataFrame(wv[wv.wv.vocab])
    wvdf.index = [key for key in wv.wv.vocab]
    wvdf.to_csv(outfile, index = True)

def essay_features_from_word_embeddings(reduced_docs_infile, embedding_infile, outfile):
    reduced_docs = utils.json_load(reduced_docs_infile)
    embedding = pd.read_csv(embedding_infile, index_col = 0)
    dft = vocab.DocFeaturizer(vocab_embedding=embedding)
    feats = dft.featurize_corpus(reduced_docs)
    feats.to_csv(outfile, index = False)