{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Create-streamlit-app.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/simplepablo/repo/blob/main/Create_streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vWmc_s2ezvU0"
      },
      "source": [
        "# Run streamlit app from a Google Colab Notebook\n",
        "> Created by [Manuel Romero](https://twitter.com/mrm8488)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RvlYkCQ9vFiy"
      },
      "source": [
        "!pip install -q streamlit"
      ],
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uzvl_5Cv8HeX"
      },
      "source": [
        "Reset the execution environment after streamlit installation"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jnZ0QpzC0UiU"
      },
      "source": [
        "## Download a streamlit app example\n",
        "\n",
        "This example comes from [How to Build a Simple Machine Learning Web App in Python](https://www.youtube.com/watch?v=8M20LyCZDOY) and it will create a **Simple Iris Flower Prediction App**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "S1sic9Rt0T7l",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3d65039f-d612-4a62-c4ef-c748d789d9bf"
      },
      "source": [
        "!wget https://raw.githubusercontent.com/dataprofessor/code/master/streamlit/iris-ml-app.py"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2022-07-27 23:20:39--  https://raw.githubusercontent.com/dataprofessor/code/master/streamlit/iris-ml-app.py\n",
            "Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...\n",
            "Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.\n",
            "HTTP request sent, awaiting response... 404 Not Found\n",
            "2022-07-27 23:20:39 ERROR 404: Not Found.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "encqGJ4u0FYG"
      },
      "source": [
        "## Install ngrok"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VSPUMEHYwqng",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f7a0c24b-50d2-4fff-fd6e-798d714ead48"
      },
      "source": [
        "!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2022-07-27 23:20:43--  https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip\n",
            "Resolving bin.equinox.io (bin.equinox.io)... 52.202.168.65, 18.205.222.128, 54.237.133.81, ...\n",
            "Connecting to bin.equinox.io (bin.equinox.io)|52.202.168.65|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 13832437 (13M) [application/octet-stream]\n",
            "Saving to: ‘ngrok-stable-linux-amd64.zip.3’\n",
            "\n",
            "ngrok-stable-linux- 100%[===================>]  13.19M  2.64MB/s    in 11s     \n",
            "\n",
            "2022-07-27 23:20:56 (1.18 MB/s) - ‘ngrok-stable-linux-amd64.zip.3’ saved [13832437/13832437]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6679q_6fwsJH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0f619b17-be35-4276-d461-828c83339ca2"
      },
      "source": [
        "!unzip ngrok-stable-linux-amd64.zip"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Archive:  ngrok-stable-linux-amd64.zip\n",
            "replace ngrok? [y]es, [n]o, [A]ll, [N]one, [r]ename: y\n",
            "  inflating: ngrok                   \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qGCM2OjvxNit"
      },
      "source": [
        "get_ipython().system_raw('./ngrok http 8501 &')"
      ],
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bxwv00hdxedU",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c9252c64-0504-4313-95eb-fef8ec29ff38"
      },
      "source": [
        "!curl -s http://localhost:4040/api/tunnels | python3 -c \\\n",
        "    'import sys, json; print(\"Execute the next cell and the go to the following URL: \" +json.load(sys.stdin)[\"tunnels\"][0][\"public_url\"])'"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Execute the next cell and the go to the following URL: https://df60-34-80-241-43.ngrok.io\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IFvZnzS4vr88",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0432d4e8-d526-47be-c74f-00bca21a80aa"
      },
      "source": [
        "!streamlit run /content/iris-ml-app.py"
      ],
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2022-07-27 23:22:17.434 INFO    numexpr.utils: NumExpr defaulting to 2 threads.\n",
            "Usage: streamlit run [OPTIONS] TARGET [ARGS]...\n",
            "\n",
            "Error: Invalid value: File does not exist: /content/iris-ml-app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WJf7BCm84KWe"
      },
      "source": [
        "[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y3VYYE)"
      ]
    }
  ]
}