import abc
from typing import List, Tuple

class ClassificationInputDataTransformer(abc.ABC):
    '''
    input: tuple of class_no, class_name, tokenized text
    '''
    @abc.abstractmethod
    def transform(self, input:Tuple[str, str, List[str]]):
        pass


class BlazingTextInputDataTransformer(ClassificationInputDataTransformer):
    '''
    https://docs.aws.amazon.com/sagemaker/latest/dg/blazingtext.html
    __label__4  linux ready for prime time , intel says , despite all the linux hype , the open-source movement has yet to make a huge splash in the desktop market . that may be about to change , thanks to chipmaking giant intel corp .
    __label__2  bowled by the slower one again , kolkata , november 14 the past caught up with sourav ganguly as the indian skippers return to international cricket was short lived .
    '''
    def __init__(self):
        self.lebel_prefix='__label__'

    def transform(self, input: Tuple[str, str, List[str]]):
        label =  self.lebel_prefix+input[1]
        text_feature = ' '.join(input[2])
        return ' '.join([label, text_feature])
