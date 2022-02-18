from multiprocessing import connection
import  urllib

CONNECTION = {}

async def websocket_application(scope, receive, send):
    while True:
        event = await receive()
        print("[event]", event)
    
        if event["type"] == "websocket.connect":
            await send ({"type": "websocket.accept"})

            query_string = scope.get("query_string", b"").decode()
            qs = urllib.parse.parse_qs(query_string)
            auth = qs.get["auth", [""]][0]

            CONNECTION[auth] = send
    
        elif event["type"] == "websocket.disconnect":
            break
        
        elif event["type"] == "websocket.receive":
            if event["text"] == "ping":
                await send({
                    "type": "websocket.send",
                    "text": "pong!"
                })
        else:
            pass
    print("[disconnect]")