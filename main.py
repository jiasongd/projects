from flask import Flask,jsonify,send_file,request
import redis
app=Flask(__name__)

def __init__():
    redis_client=redis.StrictRedis(host="localhost",port=6379,db=0,decode_responses=True)
    return redis_client


@app.route("/")
def test():
    data={"name":"dingjiasong",
          "age":"25",
          "country":"china"
    }
    return jsonify({"code":200,"message":"success","data":data})
@app.route("/test",methods=["POST"])
def test1():
    data = request.get_json()
    param1 = data.get('param1')
    param2 = data.get('param2')
    redis_cli=__init__()
    param3=param1+param2
    if redis_cli.get(param3):
        
    
    data={"value":param3}
    return jsonify({"code":200,"message":"success","data":data})

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)

    ## source venv/bin/activate