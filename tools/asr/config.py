import os
from tools.i18n.i18n import I18nAuto
i18n = I18nAuto()

def check_fw_local_models(language"pt_BR"):
    '''
    启动时检查本地是否有 Faster Whisper 模型.
    '''
    model_size_list = [
        "tiny",     "tiny.en", 
        "base",     "base.en", 
        "small",    "small.en", 
        "medium",   "medium.en", 
        "large",    "large-v1", 
        "large-v2", "large-v3"]
    for i, size in enumerate(model_size_list):
        if os.path.exists(f'tools/asr/models/faster-whisper-{size}'):
            model_size_list[i] = size + '-local'
    return model_size_list

asr_dict = {
    i18n("达摩 ASR (中文)"): {
        'lang': ['zh'],
        'size': ['large'],
        'path': 'funasr_asr.py',
    },
    i18n("Faster Whisper (多语种)"): {
        'lang': ['auto', 'zh', 'en', 'ja'],
        'size': check_fw_local_models(),
        'path': 'fasterwhisper_asr.py'
    }
}

