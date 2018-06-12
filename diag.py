import falcon
import rpy2.robjects.packages as rpackages
import rpy2.robjects as robj
import pandas as pd

# import R's utility package
utils = rpackages.importr('utils')
stats = rpackages.importr('stats')
bt = rpackages.importr('blockTools')

# dummy test data
#d = {'col1': [1, 2], 'col2': [3, 4]}
#df = pd.DataFrame(data=d)

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class DiagResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        
        # start doing stuff here
        try:
            out = bt.seqblock(query = FALSE, id_vars = "ID", id_vals = 002, exact_vars = "var1", exact_vals = "Dem", covar_vars = "var2", covar_vals = 25)
            #out = str(stats.rnorm(1))

            resp.body = out
        # if it doesn't work, tell the user what's wrong
        except Exception as e:
            resp.body = e
            
# falcon.API instances are callable WSGI apps
app = falcon.API()

app.add_route('/test', DiagResource())
