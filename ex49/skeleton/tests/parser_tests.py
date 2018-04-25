from nose.tools import *
from ex49.parser import *
from ex49.lexicon import lexicon


lexicon = lexicon()

def test_sentence():

	testCorrectSentence = lexicon.scan("kill the bear")

	correctSentence = parse_sentence(testCorrectSentence)

	assert_equal(correctSentence.subject, 'player')
	assert_equal(correctSentence.verb, 'kill')
	assert_equal(correctSentence.object, 'bear')


def test_wrong_sentence():

	testWrongSentence = lexicon.scan("the bear kill")

	assert_raises(ParseError, parse_sentence, testWrongSentence)
