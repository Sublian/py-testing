# Models

from src.models.LanguageModels import LanguageModel

def test_get_languages_not_one():
    languages=LanguageModel.get_languages()
    assert languages !=None
    
def test_get_languages_has_element():
    languages=LanguageModel.get_languages()
    assert len(languages)>0
    
def test_get_languages_check_element_length():
    languages=LanguageModel.get_languages()
    for language in languages:        
        assert len(language) >0