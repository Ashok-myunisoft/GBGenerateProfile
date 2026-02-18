import runpod

def handler(event):
    print("HANDLER WORKING", flush=True)
    print("EVENT:", event, flush=True)
    return {
        "status": "ok",
        "received": event
    }

runpod.serverless.start({"handler": handler})
