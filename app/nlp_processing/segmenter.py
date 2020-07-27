
import abc
import jieba
from typing import List
from ckiptagger import WS, POS, NER


class Segmenter(abc.ABC):
    @abc.abstractmethod
    def segment(self, text:str)->List[str]:
        'Return when animal screaming the sound hear likes'
        return NotImplemented

class JiebaSegmenter(Segmenter):
    def segment(self, text:str)->List[str]:
        toks = []
        res = jieba.cut(text, cut_all=False)
        for r in res:
            toks.append(r)
        return toks



class CKIPSegmenter(Segmenter):
    def __init__(self):
        self.ws = WS("./data")
        # self.pos = POS("./data")
        # self.ner = NER("./data")

    def segment(self, text:str)->List[str]:
        ws_results = self.ws([text])
        # pos_results = self.pos(ws_results)
        # ner_results = self.ner(ws_results, pos_results)
        return ws_results[0]


