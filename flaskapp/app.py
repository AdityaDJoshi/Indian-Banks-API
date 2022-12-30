from flask import make_response, jsonify
from imports import *

from validIFSC import isValidIFSCode
app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False
d = Counter()
df = pd.DataFrame()


@app.before_first_request
def load_data():
    global d
    global df
    df = pd.read_csv(os.path.join("static", "ifsc.csv"))
    d = Counter(df['bank_name'])


@app.route('/search/', methods=['POST', 'GET'])
def search():
    global df
    ifsc = request.args.get('ifsc', None)
    if ifsc == None:
        return make_response(jsonify("enter ifsc code"), 404)
    validIFSC = isValidIFSCode(ifsc)

    req = df.loc[df['ifsc'] == ifsc]
    req = req.to_dict(orient='records')
    if (not validIFSC) or len(req) == 0:
        return make_response(jsonify("wrong ifsc code"), 404)

    df1 = pd.DataFrame([
        [datetime.datetime.now(), ifsc, ],
    ],
        columns=['Timestamp', 'IFSC', ]
    )

    output_path = os.path.join("static", "statistics.csv")
    df1.to_csv(output_path, mode='a', header=not os.path.exists(
        output_path), index=False)

    print(req)
    return jsonify(req)


@app.route('/leaderboard/', methods=['POST', 'GET'])
def leaderboard():
    global d
    DESC = request.args.get('DESC', "True")
    fetchcount = request.args.get('fetchcount', "10")
    print(DESC, fetchcount)

    fetchcount = eval(fetchcount)
    DESC = eval(DESC)
    print("After typecasted", DESC, fetchcount)

    if DESC:
        # Will send as a dictionary but need to add the app.config['JSON_SORT_KEYS'] = False
        leaderboard = {a: b for a, b in d.most_common(fetchcount)}
    # No need to add the app.config line but will send as lists (which might be easier to index)
        leaderboard = d.most_common(fetchcount)

    else:
        leaderboard = {a: b for a, b in d.most_common()[-fetchcount:][::-1]}
        leaderboard = d.most_common()[-fetchcount:][::-1]

    print(leaderboard)

    return jsonify(leaderboard)


@app.route('/statistics/', methods=['POST', 'GET'])
def stats():

    stats_df = pd.read_csv(os.path.join("static", "statistics.csv"))

    DESC = request.args.get('DESC', "False")
    fetchcount = request.args.get('fetchcount', len(stats_df))
    print(DESC, fetchcount)

    fetchcount = min(eval(fetchcount), len(stats_df))
    DESC = eval(DESC)

    stats_df = stats_df.sort_values(by=['Timestamp'], ascending=not DESC)

    stats_df = stats_df.iloc[:fetchcount]
    return jsonify(stats_df.values.tolist())


if __name__ == '__main__':

    app.run(host='localhost', port=8008, debug=True)
