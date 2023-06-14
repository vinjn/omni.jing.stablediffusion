%~dp0\app\kit\omni.app.full.bat ^
    --/app/window/title=omni-stable-diffusion ^
    --ext-folder %~dp0\exts ^
    --ext-folder %~dp0\app\exts ^
    --ext-folder %~dp0\app\extscache ^
    --enable omni.kit.profiler.window ^
    --enable omni.kit.debug.vscode ^
    --enable omni.kit.browser.sample ^
    --enable omni.kit.window.material ^
    --enable omni.hello.world ^
    --/log/file=%~dp0\kit.log ^
    --/exts/omni.kit.registry.nucleus/registries/0/name="kit/public" ^
    --/exts/omni.kit.registry.nucleus/registries/0/url="https://d1aiacozzchaiq.cloudfront.net/exts/kit/public/104.0/" ^
    --/exts/omni.kit.registry.nucleus/registries/1/name="kit/community" ^
    --/exts/omni.kit.registry.nucleus/registries/1/url="https://dw290v42wisod.cloudfront.net/exts/kit/community" ^
    --/app/window/showStartup=false ^
    --/app/file/ignoreUnsavedOnExit=true ^
    --/app/file/ignoreUnsavedStage=true ^
    --/settings/renderer/enabled=rtx ^
    --/app/extensions/excluded/0=omni.iray.settings.core ^
    --/app/extensions/excluded/1=omni.hydra.iray ^
    --/app/extensions/excluded/2=omni.kit.splash ^
    --/app/extensions/excluded/3=omni.physx.bundle ^
    --/app/extensions/excluded/4=omni.graph.core ^
    --/app/extensions/excluded/5=omni.graph.ui ^
    --/app/extensions/excluded/7=omni.graph.examples.python ^
    --/app/extensions/excluded/8=omni.kit.telemetry ^
    --/app/extensions/excluded/9=omni.kit.multinode ^
    --/app/extensions/excluded/10=omni.kit.tool.collect ^
    --/app/settings/persistent=false ^
    %*
    
    @REM --/rtx/post/aa/op=4 ^