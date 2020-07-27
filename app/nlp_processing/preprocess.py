import abc
from typing import List, Tuple
class ClassificationCorpusPreprocessor(abc.ABC):
    '''
    input: path to input file
    return: list of tuples (class_no, class_name, text)
    '''

    @abc.abstractmethod
    def preprocess(self, file_path:str)->List[Tuple[str, str, str]]:
        pass

class TouTiaoNewsPreprocessor(ClassificationCorpusPreprocessor):
    '''
    https://github.com/skdjfla/toutiao-text-classfication-dataset.git
    example of toutiaonews docs
    _!_101_!_news_culture_!_林徽因什么理由拒绝了徐志摩而选择梁思 > 成为终身伴侣？_!_
    6552475601595269390
    _!_101_!_news_culture_!_黄杨木是什么树？_!_
    6552387648126714125
    _!_101_!_news_culture_!_上联：草根登上星光道，怎么对下联？_!_
    6552271725814350087
    _!_101_!_news_culture_!_什么是超写实绘画？_!_
    6552452982015787268
    _!_101_!_news_culture_!_松涛听雨莺婉转，下联？_!_
    '''
    def __init__(self):
        self.delimeter = '_!_'

    def preprocess(self, file_path:str) ->List[Tuple[str, str, str]]:
        file = open(file_path, 'r')
        res = []
        for l in file.readlines():
            toks = l.split(self.delimeter)
            classno = toks[1]
            classname = toks[2]
            title = toks[3]
            res.append((classno, classname, title))
        return res
import json
class TravelReviewPreprocessor(ClassificationCorpusPreprocessor):
    '''
    https://github.com/lsvih/chinese-customer-review
    {"s": "秀美恩施大峡谷，因其奇、险让人流连忘返。", "ot": "恩施大峡谷"}
    {"s": "龙鳞宫说白了，就是用多种颜色的灯光打在石钟乳上，形成五光十色的视觉效果", "ot": "龙鳞宫"}
    {"s": "回来百度方知道，舟山跨海大桥，又叫舟山大陆连岛工程，跨四座岛屿，翻九个涵>洞，穿两个隧道，全长四十八公里。", "ot": "舟山跨海大桥"}
    {"s": "　　旃檀林，又称“旃檀禅林”，位于九华街西南，背倚琵琶山，面朝化成寺。", "ot": "旃檀林"}
    {"s": "在秦家大院，看着点点滴滴的一切，探寻着耐人寻味的过去。", "ot": "秦家大院"}
    '''


    def preprocess(self, file_path:str) ->List[Tuple[str, str, str]]:
        file = open(file_path, 'r')
        res = []
        for l in file.readlines():
            obj = json.loads(l)
            classno = None
            classname = obj['ot']
            title = obj['s']
            res.append((classno, classname, title))
        return res

