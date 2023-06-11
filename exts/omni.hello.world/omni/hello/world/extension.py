import omni.ext
import omni.ui as ui
import requests
from PIL import Image, PngImagePlugin
import io
import base64
import os
import asyncio
import datetime
from pathlib import Path

cwd = os.getcwd()

# https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API
# http://127.0.0.1:7860/docs

# UI doc: https://docs.omniverse.nvidia.com/kit/docs/omni.kit.documentation.ui.style/1.0.3/overview.html
# stringfield: https://docs.omniverse.nvidia.com/prod_kit/prod_kit/programmer_ref/ui/widgets/stringfield.html

def make_txt2img_param(prompt, negative_prompt):
    param = {
        "enable_hr": False,
        "denoising_strength": 0,
        "firstphase_width": 0,
        "firstphase_height": 0,
        "hr_scale": 2,
        "hr_upscaler": "string",
        "hr_second_pass_steps": 0,
        "hr_resize_x": 0,
        "hr_resize_y": 0,
        "hr_sampler_name": "string",
        "hr_prompt": "",
        "hr_negative_prompt": "",
        "prompt": prompt,
        # "styles": [
        #     "string"
        # ],
        "seed": -1,
        "subseed": -1,
        "subseed_strength": 0,
        "seed_resize_from_h": -1,
        "seed_resize_from_w": -1,
        "sampler_name": "string",
        "batch_size": 1,
        "n_iter": 1,
        "steps": 50,
        "cfg_scale": 7,
        "width": 512,
        "height": 512,
        "restore_faces": False,
        "tiling": False,
        "do_not_save_samples": False,
        "do_not_save_grid": False,
        "negative_prompt": negative_prompt,
        "eta": 0,
        "s_min_uncond": 0,
        "s_churn": 0,
        "s_tmax": 0,
        "s_tmin": 0,
        "s_noise": 1,
        "override_settings": {},
        "override_settings_restore_afterwards": True,
        "script_args": [],
        "sampler_index": "Euler",
        "script_name": "string",
        "send_images": True,
        "save_images": False,
        "alwayson_scripts": {}
    }
    return param


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[omni.hello.world] MyExtension startup")

        self._window = ui.Window("stable diffusion", width=300, height=600)

        self.prompt_ssm = ui.SimpleStringModel()
        self.nagative_promopt_ssm = ui.SimpleStringModel()

        with self._window.frame:
            def on_txt2img():
                payload = {
                    "prompt": self.prompt_ssm.get_value_as_string(),
                    "negative_prompt": self.nagative_promopt_ssm.get_value_as_string(),
                    "steps": 10
                }

                url = "http://127.0.0.1:7860"
                response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
                r = response.json()
                print(response)
                if 'images' not in r:
                    return
                for i in r['images']:
                    image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

                    if False:
                        png_payload = {
                            "image": "data:image/png;base64," + i
                        }
                        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

                        pnginfo = PngImagePlugin.PngInfo()
                        pnginfo.add_text("parameters", response2.json().get("info"))
                    else:
                        pnginfo = None


                    directory = Path(cwd) / '_results'
                    directory.mkdir(parents=True, exist_ok=True)

                    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                    image_name = f'{cwd}/_results/{timestamp}.png'
                    image.save(image_name, pnginfo=pnginfo)
                    print(f'Saved to {image_name}')

                    self.image.source_url = image_name

            def on_apply():
                pass

            with ui.VStack():
                with omni.ui.HStack(height=0):
                    omni.ui.Label("Prompt")
                omni.ui.Spacer(height=5)

                with omni.ui.HStack(height=100):
                    self.promp = ui.StringField(model=self.prompt_ssm, multiline=False)
                omni.ui.Spacer(height=5)
    
                with omni.ui.HStack(height=0):
                    omni.ui.Label("Nagative Prompt")
                omni.ui.Spacer(height=5)

                with omni.ui.HStack(height=100):
                    self.negative_propmt = ui.StringField(model=self.nagative_promopt_ssm, multiline=False)
                omni.ui.Spacer(height=5)

                with omni.ui.HStack(height=0):
                    ui.Button("txt2img", clicked_fn=on_txt2img)
                    ui.Button("apply", clicked_fn=on_apply)
                # label = ui.Label("")
                # field.model.add_value_changed_fn(
                #     lambda m, label=label: setText(label, m.get_value_as_string()))
                # ui.Button("Reset", clicked_fn=on_reset)
                self.image = ui.Image(f'{cwd}/output.png')

    def on_shutdown(self):
        print("[omni.hello.world] MyExtension shutdown")
        self._window = None
