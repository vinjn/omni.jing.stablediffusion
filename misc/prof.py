# c:\p4\stable-diffusion-webui\venv\Scripts\activate.bat
import webui
import os

def main():
    from viztracer import VizTracer
    os.environ['COMMANDLINE_ARGS'] = "--api --xformers --add-stop-route --skip-version-check --no-hashing --skip-python-version-check --skip-torch-cuda-test --skip-install"
    tracer = VizTracer()
    tracer.start()
    webui.webui()
    tracer.stop()
    tracer.save() # also takes output_file as an optional argument

if __name__ == "__main__":
    main()

