from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

setup(
    name="string2string",
    version="0.0.150",
    description="String-to-String Algorithms for Natural Language Processing",
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://github.com/stanfordnlp/string2string",
    author="Mirac Suzgun",
    author_email="msuzgun@cs.stanford.edu",
    license="MIT",
    python_requires='>=3.7',
    packages=find_packages(),
    install_requires=[
        "torch",
        "numpy",
        "transformers",
        "datasets",
        "faiss-cpu==1.7.3",
        "bert_score",
        "pandas",
        "joblib",
    ],
    tests_require=["pytest"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    keywords=[
        "string matching",
        "pattern matching",
        "edit distance",
        "string to string correction",
        "string to string matching",
        "Levenshtein edit distance",
        "Hamming distance",
        "Damerau-Levenshtein distance",
        "Jaro-Winkler distance",
        "longest common subsequence",
        "longest common substring",
        "dynamic programming",
        "approximate string matching",
        "semantic similarity",
        "natural language processing",
        "NLP",
        "information retrieval",
        "rouge",
        "sacrebleu",
        "bertscore",
        "bartscore",
        "fasttext",
        "glove",
        "cosine similarity",
        "Smith-Waterman",
        "Needleman-Wunsch",
        "Hirschberg",
        "Karp-Rabin",
        "Knuth-Morris-Pratt",
        "Boyer-Moore",
    ],
)
