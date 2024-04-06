from brainscore_vision import score
import os


for i in range(4):
    for j in range(40):
        try:
            model_score = score(
                model_identifier=f'cornet_s_{i}_{j}_4096',
                benchmark_identifier='MajajHong2015public.V4-pls'
            )
            print(model_score)
        except:
            print(f'{i}_{j} did not work')
