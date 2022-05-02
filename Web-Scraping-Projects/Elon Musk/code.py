import twint

c = twint.Config()

c.Username = "naval"
#c.Search = ['naval ravikant']       # topic

c.Links = "exclude"     # Delete tweets with links
c.Filter_retweets = True # Exclude retweets from the results.
c.Lang = "en"
c.Since = "2015-11-01 00:00:00"
c.Until = "2022-11-01 00:00:00"
c.Custom = ["conversation_id","date", "time", "username", "tweet","replies_count","retweets_count","likes_count","link"]
c.Store_csv = True       # store tweets in a csv file
c.Output = "naval-today.csv"     # path to csv file
c.Hide_output=True

twint.run.Search(c)