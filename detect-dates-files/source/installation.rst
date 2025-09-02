Installation
===========

This guide covers the installation of the Arabic Date Module package and its dependencies.

Requirements
-----------

- Python 3.8 or higher
- pip package manager
- Operating system: Windows, Linux, or macOS

Basic Installation
----------------

Install using pip::

    pip install ar-date-module

This will install the latest stable version with all required dependencies.

Development Installation
----------------------

For development work, clone the repository and install in editable mode::

    git clone https://github.com/mlotfi/ar-date-module.git
    cd ar-date-module
    pip install -e .[dev]

The ``[dev]`` extra will install additional dependencies needed for development:

- pytest
- sphinx
- black
- flake8

Virtual Environment
-----------------

It's recommended to use a virtual environment::

    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/macOS
    python -m venv venv
    source venv/bin/activate

Docker Installation
-----------------

A Docker image is also available::

    docker pull mlotfi/ar-date-module
    docker run -it mlotfi/ar-date-module

Configuration
------------

No additional configuration is required for basic usage. For advanced settings, 
see the :doc:`configuration guide </user-guide/configuration>`.

Troubleshooting
--------------

Common Installation Issues
~~~~~~~~~~~~~~~~~~~~~~~~

1. **Dependency Conflicts**

   If you encounter dependency conflicts, try installing in a fresh virtual environment::

       python -m venv fresh-env
       .\fresh-env\Scripts\activate
       pip install ar-date-module

2. **Compilation Issues**

   On Windows, ensure you have the appropriate Visual C++ build tools installed::

       pip install --upgrade setuptools wheel
       pip install ar-date-module

3. **Version Compatibility**

   Check Python version compatibility::

       python --version
       pip list | findstr ar-date-module

Getting Help
-----------

If you encounter any issues:

1. Check the :doc:`FAQ </user-guide/faq>` section
2. Search existing `GitHub Issues <https://github.com/mlotfi/ar-date-module/issues>`_
3. Open a new issue if needed

Next Steps
---------

- :doc:`Quick Start Guide </user-guide/quickstart>`
- :doc:`Usage Examples </user-guide/examples>`
- :doc:`API Reference </api/index>`

{%- extends "sphinx_rtd_theme/breadcrumbs.html" %}

{%- block breadcrumbs_aside %}
  <li class="wy-breadcrumbs-aside">
    <a href="https://github.com/mlotfi/ar-date-module/edit/main/docs/{{ pagename }}.rst" 
       class="fa fa-github"> Edit on GitHub</a>
  </li>
{%- endblock %}