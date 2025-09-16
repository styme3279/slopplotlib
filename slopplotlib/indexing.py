from matplotlib.collections import PathCollection as Plot
from typing import Optional, Tuple



def slopplotlib(prompt : str, data, model : str, return_code : bool = False, run_code : bool = False) -> Optional[Plot] | Optional[Tuple[str,Plot]]:
    """
    Generate a matplotlib plot based on a text prompt using a language model.

    Parameters:
    - prompt (str): The text prompt describing the desired plot.
    - model (str): The language model to use for generating the code. Formatted as e.g. "openai/gpt-4" or "openrouter/google/gemini-2.5-flash"
    - return_code (bool): If True, return the generated code as a string.
    - run_code (bool): If True, execute the generated code and return the plot object.

    Returns:
    - Optional[Plot]: The generated plot object if run_code is True, otherwise None.
    """
    try:
        import matplotlib
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError("matplotlib is required for using slopplotlib. Please install it via 'pip install matplotlib'.")
    
    model_param = [i for i in model.split("/")]
    if len(model_param) == 2:
        provider, model_name = model_param
    elif len(model_param) == 3:
        provider, organization, model_name = model_param
    else:
        raise ValueError("Model parameter must be in the format 'provider/model_name' or 'provider/organization/model_name'")
    
    if provider.lower() == "openai":
        try: 
            from openai import OpenAI
        except:
            raise ImportError("OpenAI package is required for using OpenAI models. Please install it via 'pip install openai'.")
        try: 
            client = OpenAI()
        except:
            raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": "The user will ask you to create a plot based on the following guidelines:\n" + prompt + "\n\n The data for generating this plot is provided as follows here:\n" + str(data) + "\n\n You must generate a matplotlib code to create this plot. Ensure that the code is complete and can be run as is. You may first think about how to plot the data and meet the user's request to the best of your ability. Format your code as follows ```python\n<your code here>\n```. Your code must take exactly one argument, which is the data provided above. The argument must be named 'data'. The code must return a matplotlib PathCollection object. When run using exec(), the plot object should be assigned to a variable named `plot`. Matplotlib and Matplotlib.pyplot are already imported as `import matplotlib` and `import matplotlib.pyplot as plt`. Do not use any other libraries. Do not try to render the plot, or call plot.show(). Just generate the plot object and set it equal to the variable named `plot`. The data will be given in the environment as the variable `data`. So you do not need to import or define it."},
            ]
        )
        
        generated_code = response.choices[0].message.content.strip().split("```python")[1].split("```")[0].strip()
        
        
        
        if run_code and not return_code:
            print(generated_code)
            import matplotlib.pyplot as plt
            namespace = {'plt': plt, 'data': data}
            exec(generated_code, namespace)
            return namespace['plot']
        if return_code and not run_code:
            return generated_code
        if return_code and run_code:
            namespace = {'plt': plt, 'data': data}
            exec(generated_code, namespace)
            return generated_code, namespace['plot']


def sloply(prompt : str, data, model : str, return_code : bool = False, run_code : bool = False) -> Optional[Plot]:
    """
    Generate a matplotlib plot based on a text prompt using a language model.

    Parameters:
    - prompt (str): The text prompt describing the desired plot.
    - model (str): The language model to use for generating the code. Formatted as e.g. "openai/gpt-4" or "openrouter/google/gemini-2.5-flash"
    - return_code (bool): If True, return the generated code as a string.
    - run_code (bool): If True, execute the generated code and return the plot object.

    Returns:
    - Optional[Plot]: The generated plot object if run_code is True, otherwise None.
    """
    try:
        import plotly.express as px
        import plotly.graph_objects as go
    except ImportError:
        raise ImportError("plotly is required for using sloply. Please install it via 'pip install plotly'.")
    model_param = [i for i in model.split("/")]
    if len(model_param) == 2:
        provider, model_name = model_param
    elif len(model_param) == 3:
        provider, organization, model_name = model_param
    else:
        raise ValueError("Model parameter must be in the format 'provider/model_name' or 'provider/organization/model_name'")
    
    if provider.lower() == "openai":
        try: 
            from openai import OpenAI
        except:
            raise ImportError("OpenAI package is required for using OpenAI models. Please install it via 'pip install openai'.")
        try: 
            client = OpenAI()
        except:
            raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": "The user will ask you to create a plot based on the following guidelines:\n" + prompt + "\n\n The data for generating this plot is provided as follows here:\n" + data + "\n\n You must generate plotly code to create this plot. You may begin by thinking about how to plot the data and meet the user's request to the best of your ability. Always format your code as follows ```python\n<your code here>\n```. Your code must take exactly one argument, which is the data provided above. The argument must be named 'data'. The code must set a variable named `fig` to a plotly figure object. `plotly.express` is already imported as `px` and `plotly.graph_objects` is already imported as `go`. Do not use any other libraries. Do not try to render the plot, or call fig.show(). Just generate the figure object and set it equal to the variable named `fig`. The data will be given in the environment as the variable `data`. So you do not need to import or define it."},
            ]
        )
        
        generated_code = response.choices[0].message.content.strip().split("```python")[1].split("```")[0].strip()

        if run_code and not return_code:
            print(generated_code)
            namespace = {'px': px, 'go': go, 'data': data}
            exec(generated_code, namespace)
            return namespace['fig']
        if return_code and not run_code:
            return generated_code
        if return_code and run_code:
            namespace = {'px': px, 'go': go, 'data': data}
            exec(generated_code, namespace)
            return generated_code, namespace['fig']    