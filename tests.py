from requests import post as make_post_request

def make_requests(url: str) -> None:
    expressions = ["2*(2+2)", #8
                   "(2+2)*2", #8
                   "(2+2+(2*2+2))*2", #20
                   "43/5+15*2-36", # 2,6
                   "42/2/7/3", #1
                   "2*(2+2)*2+1/10-0.1+2^4"] # 32
    
    for expression in expressions:
        post_object = {
            "expression": expression
        }
        response = make_post_request(url, json=post_object)
        print(response.text)

if __name__ == "__main__":
    url = "http://localhost:5000"
    make_requests(url)
