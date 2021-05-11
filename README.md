# CS 470 - Dask

## Introduction
Dask is a parallel computing library for Python. One of Dask’s key features is its extension of common big data structure interfaces, including NumPy, Pandas, and Python iterators. Dask takes these ideas and extends them to larger-than-memory and distributed computing environments.  Like paradigms we have discussed this semester, Dask supports running on anywhere from a single laptop to a distributed cluster of hundreds of machines.<sup>1</sup> A crucial “under the covers” cog in the Dask machine is how it handles task scheduling. Dask uses dynamic task scheduling with a Task Graph. When using Dask, like any doing any parallel programming, a program is broken down into many smaller tasks. These tasks are then represented in a Task Graph as nodes. Dependencies with other nodes, or tasks, is shown with edges. Dask’s task scheduler then executes this graph to ensure proper dependencies and use parallelism whenever possible.<sup>2</sup> Compared to other paradigms we have looked at this semester, Dask does not require as much user defined parallel actions, like the compiler directives in OpenMP. This also has to do with Python being run in an interpreter rather than first going through a compiler then being run. One major difference between Dask and topics we have covered, such as OpenMP and MPI, is that Dask is designed to be able to be used interactively, while the other topics (mainly due to language constraints) cannot run interactively. Like OpenMP, a lot of the details of parallelism in Dask are accomplished behind the scenes away from the programmer. In Dask this is the Task Graph and scheduler, while in OpenMP it the compiler. Many applications are based around using data structures and libraries, such as NumPy, that Dask extends. Building support for these structures in the core of Dask allows for programmers to easily convert their serial programs running on a single machine to parallel programs running on many machines. In many cases it could be as easy as changing an import statement to use Dask’s extended structure instead of the original. Like all of paradigms we have covered this semester, Dask is being used in a wide variety of applications. One application is in the SatPy library developed by David Hoese at the Space Science and Engineering Center at UW-Madison. Some issues that SatPy was having was very long execution times on non-high performance computing systems and running out of space in memory. By switching to using Dask’s DataArray objects and its other capabilities, SatPy is now able to create high resolution images in under 10 minutes on older laptops that would have crashed after 35 minutes using the old non-Dask implementation.<sup>3</sup> 

<sup>1</sup> https://docs.dask.org/en/latest/

<sup>2</sup> https://docs.dask.org/en/latest/graphs.html

<sup>3</sup> https://stories.dask.org/en/latest/satellite-imagery.html

## Installation

1. In order to install and use Dask, users must first have Python installed. To check if you have Python installed and installed correctly, open a terminal/command prompt and type `python --version`. If this results in printing `3.x.x` you can skip the next step. If it results in `2.x.x` or an error, continue with the next step to install Python.

2. Installing Python:

    a. To install Python in Windows, go to the [Python for Windows page](https://www.python.org/downloads/windows/) and download the latest stable release “Windows installer” for your computer, be sure to correctly choose 64-bit or 32-bit depending on your machine (See [here](https://support.microsoft.com/en-us/windows/32-bit-and-64-bit-windows-frequently-asked-questions-c6ca9541-8dce-4d48-0415-94a3faa2e13d) for how to determine the correct type).
    
    b. To install Python in Mac, go to the [Python for Mac page](https://www.python.org/downloads/mac-osx/) and download the latest stable release installer.
    
    c. To install Python in Linux, see the Linux section [here](https://wiki.python.org/moin/BeginnersGuide/Download) for instructions for your OS.
    
    d. For more details and options see [here](https://wiki.python.org/moin/BeginnersGuide/Download).
    
3. Now that you have Python installed we can install Dask. In a terminal/command prompt enter the command `python -m pip install "dask[complete]"` to install Dask.

4. (Optional) Install [Visual Studio Code](https://code.visualstudio.com/) and the Python extension to allow for easy Python development. See [here](https://code.visualstudio.com/docs/editor/extension-marketplace ) for more details on how to install the Python extension for VS Code.

## Hello World

This simple Hello World program `hello_world.py` demonstrates the basic capabilities of Dask by printing some words. This example program is based on Dask’s Delayed example, which can be found [here](https://docs.dask.org/en/latest/delayed.html).

1. First, download the `hello_world.py` program from this repo, located [here](https://github.com/jwritz-uwl/cs-470-dask/blob/main/hello_world.py).
2. Run the program as is. If you are using a terminal/command prompt use `python hello_world.py` in the directory containing the program. If you are using Visual Studio Code, simply open the program and click the green "Run" triangle in the top right corner of the window. This will print "Hello World!", "Hello", "World", and "hello world". "Hello" and "World" may vary in order, for similar reasons that we saw when using pthreads.
3. To better understand what the delayed function is doing, play around with the program by modifying the sleep values and observing the results.

What does this dask.delayed function do? One of the key pieces of Dask is its Task Graph. The Task Graph is a graph (similar to a flow chart) with nodes that represent different tasks. The delayed function is used to create a graph. When x and y are assigned, they each are their own graph since they are not connected. When z is assigned however, since both x and y are parameters, and hence required to occur before say in z, they are connected to z in its graph. When z.compute is called, the graph is worked through, so before z’s function can be called x and y’s must be called first. 

## Advanced Tutorial

For this advanced tutorial program we will demonstrate an image processing application of Dask.  We will be taking an input image, splitting it into chunks, and performing a grayscale transformation to each chunk before rearranging it back into an output image.  This tutorial can be followed along here or on the Dask website found [here](https://examples.dask.org/applications/image-processing.html).


![input image](https://github.com/jwritz-uwl/cs-470-dask/blob/main/images/astronaut.png)

![output image](https://github.com/jwritz-uwl/cs-470-dask/images/blob/main/astronaut_grayscale.png)


1. First make sure that these dependencies are installed as we will need them all for the later steps.
    - `pip install dask_image`
    - `pip install -U matplotlib`
    - `pip install scikit-image --upgrade-strategy only-if-needed`
2. The next step is creating a folder where we will manipulate these images.  For this example, we will make a folder within our project directory named images.  This can be done easily with `mkdir images`.
3. Now, we will run `import_images.py` which will split up our astronaut image into four equal sized chunks to be parallelly processed.  The output of this program will be those four images in the images folder we created in the previous step.

![corner image](https://github.com/jwritz-uwl/cs-470-dask/blob/main/images/image-00.png)

4. Lastly, all we have to do to process this image is to run `grayscale.py`.  The first part of this program is a method called pixelTransform(rgb) which returns an array of grayscale values corresponding to their color equivalents.  Next, the image data is read into a list of images that match the pattern specified.  This list is fed into the pixelTransform method where all the parallelized work is done.  Finally, we can combine this data back into one image to be displayed with matplotlib.
5. Additional effects can be achieved by playing around with the pixelTransform method.  For some practice you can try and extract only certain bands of color from the image to see what those results look like.  An example of extracting just the red band can be found [here](https://github.com/jwritz-uwl/cs-470-dask/blob/main/red_extract.py).