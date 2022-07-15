=====================
Setting up the models
=====================

Dispersion model (DM)
---------------------
.. code-block:: python

    from transep import transep
    import numpy as np

    input = np.zeros((100,))
    input[0] = 30
    output = transep.simulate(input, transep.dispersion_function, 1, p_d=0.1, mtt=100)

Exponential piston model (EPM)
------------------------------
.. code-block:: python

    from transep import transep
    import numpy as np

    input = np.zeros((100,))
    input[0] = 30
    output = transep.simulate(input, transep.gamma_function, 1, mtt=100, eta=0.1)

Gamma model (GM)
----------------
.. code-block:: python

    from transep import transep
    import numpy as np

    input = np.zeros((100,))
    input[0] = 30
    output = transep.simulate(input, transep.gamma_function, 1, alpha=1, beta=1)

Linear reservoir model (LRM)
----------------------------
.. code-block:: python

      from transep import transep
      import numpy as np

      input = np.zeros((100,))
      input[0] = 30
      output = transep.simulate(input, transep.linear_reservoir_function, 1, mtt=40)

Parallel linear reservoir model (PLRM)
--------------------------------------
.. code-block:: python

      from transep import transep
      import numpy as np

      input = np.zeros((100,))
      input[0] = 30
      output = transep.simulate(input, transep.parallel_linear_reservoir_function, 1, mtt_slow=60, mtt_fast=10, frac_fast=0.1)
