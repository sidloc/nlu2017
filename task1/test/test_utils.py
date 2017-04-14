import sys
sys.path.append('../src')
import unittest
from utils import SentenceCleaner
from utils import DataLoader

class SentenceCleanerTest(unittest.TestCase):


     if __name__ == '__main__':
          unittest.main()

     def setUp(self):
          self.cleaner = SentenceCleaner()

     def test_SentenceCleaner_array_starts_with_bos(self):
          sentence = "lorem ipsum dolor sit amet , consetetur"
          append_split = self.cleaner.prepare_sentence(sentence)
          assert append_split[0] == self.cleaner.INIT_SEQ

     def test_SentenceCleaner_array_ends_with_is_eos(self):
          sentence = "lorem ipsum dolor sit amet , consetetur"
          append_split = self.cleaner.prepare_sentence(sentence)
          assert append_split[-1] == self.cleaner.END_SEQ

     def test_SentenceCleaner_returns_array_with_shape_30(self):
          sentence = "Aliquam ut mattis felis , vel accumsan orci . Donec arcu dolor , luctus in nibh id , rutrum consequat elit . Phasellus sed dolor maximus , euismod quam sed , varius tellus . Fusce condimentum libero in ante lobortis"
          append_split = self.cleaner.prepare_sentence(sentence)
          assert append_split.shape[0] == self.cleaner.LENGTH


     def test_array_is_padded(self):
          sentence = "lorem ipsum dolor sit amet , consetetur"
          ar = self.cleaner.prepare_sentence(sentence)
          for i in range(8,29):
               assert ar[i] == self.cleaner.PADDING




class DataLoaderTest(unittest.TestCase):
     if __name__ == '__main__':
          unittest.main()

     def setUp(self):
          self.loader = DataLoader()

     def test_loadFileIntoMemory(self):
          self.loader.load_data("./testfile.txt")
          assert self.loader.data is not None
          assert self.loader.data.shape == (5, 30)