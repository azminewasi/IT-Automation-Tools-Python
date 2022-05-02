import time
import twint


c = twint.Config()
c.Username = "naval"
c.Links = "exclude"      # Delete tweets with links
c.Filter_retweets = True # Exclude retweets from the results.
c.Lang = "en"            # Tweets in English only

c.Since = "2015-11-01 00:00:00"
c.Until = "2022-11-01 00:00:00"

c.Custom = ["conversation_id","date", "time", "username", "tweet","replies_count","retweets_count","likes_count","link"]
c.Output = "naval-today.csv"
c.Hide_output = True     # Output will not be shown in console
twint.run.Search(c)      # Run