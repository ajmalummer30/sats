import websocket
import threading
import time

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("### WebSocket closed ###")

def on_open(ws):
    def run(*args):
        while True:
            message = input("Enter message to send (type 'exit' to quit): ")
            if message == "exit":
                ws.close()
                break
            else:
                ws.send(message)
                time.sleep(1)

    threading.Thread(target=run).start()

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8000/ws/test/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()