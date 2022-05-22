Filename: /Users/kirilldenisov/Desktop/course.vk.deep_python/08.Profiling/profiling.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    52     44.6 MiB     44.6 MiB           1   @memory_profiler.profile
    53                                         def mem_stat():
    54     49.6 MiB      5.0 MiB           1       create_original()
    55     51.5 MiB      1.9 MiB           1       create_slots()
    56     54.8 MiB      3.3 MiB           1       create_weakref()


```
          800007 function calls in 0.675 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.026    0.026    0.491    0.491 profiling.py:48(create_weakref)
        1    0.012    0.012    0.466    0.466 profiling.py:49(<listcomp>)
   100000    0.032    0.000    0.454    0.000 profiling.py:37(__init__)
   100000    0.265    0.000    0.422    0.000 /opt/homebrew/Caskroom/miniforge/base/envs/web/lib/python3.9/weakref.py:105(__init__)
   100000    0.038    0.000    0.156    0.000 /opt/homebrew/Caskroom/miniforge/base/envs/web/lib/python3.9/weakref.py:290(update)
   200000    0.115    0.000    0.115    0.000 {method 'items' of 'dict' objects}
        1    0.015    0.015    0.103    0.103 profiling.py:42(create_original)
   200000    0.102    0.000    0.102    0.000 profiling.py:11(__init__)
        1    0.029    0.029    0.088    0.088 profiling.py:43(<listcomp>)
        1    0.013    0.013    0.081    0.081 profiling.py:45(create_slots)
        1    0.025    0.025    0.068    0.068 profiling.py:46(<listcomp>)
   100000    0.003    0.000    0.003    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


 ```
