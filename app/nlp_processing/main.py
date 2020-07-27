from preprocess import TouTiaoNewsPreprocessor
from segmenter import CKIPSegmenter
from transformer import BlazingTextInputDataTransformer
from preprocess import TravelReviewPreprocessor

preprocessor = TravelReviewPreprocessor()
res = preprocessor.preprocess('/Users/yianc/clients/5jcj86/chinese-customer-review/mafengwo/train.txt')
segmenter = CKIPSegmenter()
transformer = BlazingTextInputDataTransformer()
for r in res:
    toks = segmenter.segment(r[2])
    input = transformer.transform((r[0], r[1], toks))
    print(input)