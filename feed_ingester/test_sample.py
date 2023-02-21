from feed_ingester import *

def test_answer():
    assert scrapeArticle("valid", "valid") == "success"
    assert scrapeArticle("invalid", "invalid") == "failed"
    assert scrapeArticle("valid", "invalid") == "failed"
    assert scrapeArticle("invalid", "valid") == "failed"

    assert scraperInterface("valid") == "success"
    assert scraperInterface("invalid") == "failed"

    assert sentimentAnalzye("valid") == "success"
    assert sentimentAnalzye("invalid") == "failed"