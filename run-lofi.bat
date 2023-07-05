%~dp0\run.bat ^
    --/rtx/post/aa/op=0 ^
    --/app/renderer/skipMaterialLoading=true ^
    --/rtx/reflections/enabled=false ^
    --/rtx/translucency/enabled=false ^
    --/rtx/post/lensFlares/enabled=false ^
    --/rtx/post/dof/enabled=false ^
    --/rtx/ambientOcclusion/enabled=false ^
    --/rtx/reflections/sampledLighting/samplesPerPixel=1 ^
    --/rtx/indirectDiffuse/enabled=false ^
    %*
    