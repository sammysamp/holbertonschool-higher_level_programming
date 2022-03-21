
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="google" content="notranslate">

    <title>Project: 0x00. Python - Hello, World | Holberton Peru Intranet</title>

      <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">
      <link rel="stylesheet" media="all" href="/assets/application-b3013969e481bb021a1efc260d98c6eaf819325cb85287559923dbd881cf89fe.css" />
      <script src="https://www.gstatic.com/charts/loader.js"></script>
      <script src="/assets/application-09f8171f2bad7bcbede10f99d481fc3dd707e27b0a03adcaa764f5579ed7dab7.js"></script>
      <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" />
      <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="c13N7orgY1ZO3pZyleqX3mbZ0//8pqKOvPx/zCs2BYo8JxMHWa9WdCnO9TfS47dRGNmsRYTgS1/yjMwY8DkKsQ==" />

      <link rel="apple-touch-icon" href="/apple-touch-icon.png">

      <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
      <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->

      <!-- Store user timezone -->
      <script>
        Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
      </script>

      <!-- intro.js for interactive onboarding -->

      <!-- React -->
      <script src="/packs/js/application-45ae50bf692bc9a3f4c3.js"></script>
      <link rel="stylesheet" media="screen" href="/packs/css/application-f61adf9f.css" />

  </head>

  <body class="
    signed_in
    env_production
    
    "
    translate="no"
    class="notranslate"
    data-theme-suffix=""
    data-checker-special-theme="womens_history_month">

      <input type="hidden" id="hbtn-slack-url" value="https://holberton.enterprise.slack.com">
      <nav class="navbar navbar-default navbar-fixed-top topbar visible-xs">
  <div class="navbar-header">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-mobile" aria-expanded="false">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>

    <a class="navbar-brand" href="/">
      <div class="logo"></div>
</a>  </div>

  <div class="collapse navbar-collapse navigation" id="navbar-mobile">
    <ul class="nav navbar-nav">
      
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i aria-hidden="true" class="fa fa-info-circle "></i></div><div class="visible-xs">Help</div></a></li>


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Planning"><a href="/dashboards/my_planning"><div class="icon "><i aria-hidden="true" class="fa fa-calendar "></i></div><div class="visible-xs">Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="My reports"><a href="/users/my_reports"><div class="icon "><i aria-hidden="true" class="fa fa-sticky-note-o "></i></div><div class="visible-xs">My reports</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Mock interviews"><a href="/dashboards/my_current_reefineries"><div class="icon "><i aria-hidden="true" class="fa fa-commenting-o "></i></div><div class="visible-xs">Mock interviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i aria-hidden="true" class="fa fa-graduation-cap "></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i aria-hidden="true" class="fa fa-comments "></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/user_containers/current"><div class="icon "><i aria-hidden="true" class="fa fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i aria-hidden="true" class="fa fa-wrench "></i></div><div class="visible-xs">Tools</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Video on demand"><a href="/dashboards/videos"><div class="icon "><i aria-hidden="true" class="fa fa-film "></i></div><div class="visible-xs">Video on demand</div></a></li>

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa fa-book "></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Officers"><a href="/dashboards/my_officers"><div class="icon "><i aria-hidden="true" class="fa fa-building "></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Speakers of the Day"><a href="/dashboards/my_speakers_of_the_day"><div class="icon "><i aria-hidden="true" class="fa fa-microphone "></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Slack">
      <a target="_blank" href="https://holberton.enterprise.slack.com">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://holbertonintranet.s3.amazonaws.com/users/photos/000/003/400/thumb/Sammy01.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220321%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220321T193208Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=51bd264d2c62a1b2f34b03962182f7241c3a8e21e0dc9d117be12d41b1db0b2d')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


    </ul>
  </div>
</nav>

      <div class="hidden-xs navigation sidebar">
  <a class="logo-container" href="/">
    <div class="logo"></div>
</a>
  <ul>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Help"><a target="_blank" href="https://students-support.hbtn.io/hc"><div class="icon "><i aria-hidden="true" class="fa fa-info-circle "></i></div><div class="visible-xs">Help</div></a></li>


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Planning"><a href="/dashboards/my_planning"><div class="icon "><i aria-hidden="true" class="fa fa-calendar "></i></div><div class="visible-xs">Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="My reports"><a href="/users/my_reports"><div class="icon "><i aria-hidden="true" class="fa fa-sticky-note-o "></i></div><div class="visible-xs">My reports</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Mock interviews"><a href="/dashboards/my_current_reefineries"><div class="icon "><i aria-hidden="true" class="fa fa-commenting-o "></i></div><div class="visible-xs">Mock interviews</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i aria-hidden="true" class="fa fa-graduation-cap "></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i aria-hidden="true" class="fa fa-comments "></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/user_containers/current"><div class="icon "><i aria-hidden="true" class="fa fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i aria-hidden="true" class="fa fa-wrench "></i></div><div class="visible-xs">Tools</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Video on demand"><a href="/dashboards/videos"><div class="icon "><i aria-hidden="true" class="fa fa-film "></i></div><div class="visible-xs">Video on demand</div></a></li>

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa fa-book "></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Officers"><a href="/dashboards/my_officers"><div class="icon "><i aria-hidden="true" class="fa fa-building "></i></div><div class="visible-xs">Officers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Speakers of the Day"><a href="/dashboards/my_speakers_of_the_day"><div class="icon "><i aria-hidden="true" class="fa fa-microphone "></i></div><div class="visible-xs">Speakers of the Day</div></a></li>


<hr class="visible-xs">

<li>
    <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Slack">
      <a target="_blank" href="https://holberton.enterprise.slack.com">
        <div class="image slack">
          <div class="inner"></div>
        </div>
        <div class="visible-xs">Slack</div>
</a>    </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://holbertonintranet.s3.amazonaws.com/users/photos/000/003/400/thumb/Sammy01.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220321%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220321T193208Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=51bd264d2c62a1b2f34b03962182f7241c3a8e21e0dc9d117be12d41b1db0b2d')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


  </ul>
</div>


    <main>
      <div id="layout-bars">
        

        

        

        
      </div>

      <article class="">

        
<div class="project row">
  <div class="col-xs-12 col-md-10 col-lg-8 contains-images">

      <h1 class="gap">0x00. Python - Hello, World</h1>

  <div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[]}" data-react-cache-id="tags/Tags-0"></div>

  <ul class="list-group metadata" id="project-metadata">

    <li class="list-group-item">
      <i aria-hidden="true" class="fa fa-user  fa-fw"></i>
      By Guillaume
    </li>

    <li class="list-group-item">
      <i aria-hidden="true" class="fa fa-cogs  fa-fw"></i>
      Weight: 1
    </li>



      <li class="list-group-item">
        <i aria-hidden="true" class="fa fa-calendar  fa-fw"></i>
          Project over - took place from 09-06-2021 to 09-07-2021
          - you're done with <span id="student_task_done_percentage">191</span>% of tasks.
      </li>



      <li class="list-group-item">
        <i aria-hidden="true" class="fa fa-check-square  fa-fw"></i>
        An auto review will be launched at the deadline
      </li>

      <div class="gap clean well">
  <h4>In a nutshell&hellip;</h4>
  <ul>


      <li>
        <strong>Auto QA review:</strong>
          79.65/89 mandatory
            &
            17.55/27 optional
      </li>
    <li>
      <strong>Altogether:</strong>
        &nbsp;<strong>147.66%</strong>
        <ul>
          <li>Mandatory: 89.49%</li>
            <li>Optional: 65.0%</li>
            <li>
              Calculation:&nbsp;
                  89.49%
                    + (89.49% * 65.0%)
              &nbsp;==&nbsp;<strong>147.66%</strong>
            </li>
        </ul>
    </li>
  </ul>
</div>

</ul>




    <div id="project_id" style="display: none" data-project-id="231"></div>




      

        <h2>Concepts</h2>

  <div class="panel panel-default">
    <div class="panel-body">
      <p>
        <em>For this project, students are expected to look at these concepts:</em>
      </p>

      <ul>
          <li>
            <a href="/concepts/63">Python programming </a>
          </li>
          <li>
            <a href="/concepts/550">Python programming </a>
          </li>
          <li>
            <a href="/concepts/551">Python programming</a>
          </li>
      </ul>
    </div>
  </div>


      <div class="well clean" id="project-description">
  <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg" alt="" style="" /></p>

<h2>Author’s disclaimer</h2>

<pre><code>Welcome to the Python world!

The first projects are more &quot;C-oriented&quot; - no tricks, no funky syntax - simple!
If you&#39;ve already played with Python, don&#39;t worry, fun things will come.
You&#39;ll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode. At Holberton, we won&#39;t start off with using PyCode, because it&#39;s much more strict compared to PEP8. Don&#39;t worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

- Guillaume
</code></pre>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/3mNweasE_b9U8vtCCFVB2g" title="The Python tutorial" target="_blank">The Python tutorial</a> (<em>only the first three chapters below</em>)</li>
<li><a href="/rltoken/FRNro28k4Q_zlkpW_si2pw" title="Whetting Your Appetite" target="_blank">Whetting Your Appetite</a> </li>
<li><a href="/rltoken/M04rBQ5xGZtZ9yjaZsHxcA" title="Using the Python Interpreter" target="_blank">Using the Python Interpreter</a> </li>
<li><a href="/rltoken/zVN1z9aa8L8jBhSp2AdbHw" title="An Informal Introduction to Python" target="_blank">An Informal Introduction to Python</a> (<em>Read up until &ldquo;3.1.2. Strings&rdquo; included</em>)</li>
<li><a href="/rltoken/z6mk3Yep2tJVSF6KsBAYrg" title="How To Use String Formatters in Python 3" target="_blank">How To Use String Formatters in Python 3</a> </li>
<li><a href="/rltoken/gYgGXOth8N16KjUpXgO1uQ" title="Learn to Program" target="_blank">Learn to Program</a> </li>
<li><a href="/rltoken/fSEQ7fsRWu0uFg_wRR4KhQ" title="Pycodestyle -- Style Guide for Python Code" target="_blank">Pycodestyle &ndash; Style Guide for Python Code</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/xmqgbvTwSBDY_bN0pnDXeQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>Who created Python</li>
<li>Who is Guido van Rossum</li>
<li>Where does the name &lsquo;Python&rsquo; come from</li>
<li>What is the Zen of Python</li>
<li>How to use the Python interpreter</li>
<li>How to print text and variables using <code>print</code></li>
<li>How to use strings</li>
<li>What are indexing and slicing in Python</li>
<li>What is the official Python coding style and how to check your code with <code>pycodestyle</code></li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file at the root of the repo, containing a description of the repository</li>
<li>A <code>README.md</code> file, at the root of the folder of <em>this</em> project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h3>Shell Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
<li>All your scripts should be exactly two lines long (<code>wc -l file</code> should print 2)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/bin/bash</code></li>
<li>All your files must be executable</li>
</ul>

<h3>C Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89</li>
<li>All your files should end with a new line</li>
<li>Your code should use the <code>Betty</code> style. It will be checked using <a href="https://github.com/holbertonschool/Betty/blob/master/betty-style.pl" title="betty-style.pl" target="_blank">betty-style.pl</a> and <a href="https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl" title="betty-doc.pl" target="_blank">betty-doc.pl</a></li>
<li>You are not allowed to use global variables</li>
<li>No more than 5 functions per file</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don&rsquo;t have to push them to your repo (if you do we won&rsquo;t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions should be included in your header file called <code>lists.h</code></li>
<li>Don’t forget to push your header file</li>
<li>All your header files should be include guarded</li>
</ul>

<h2>More Info</h2>

<h3>Zen</h3>

<pre><code>The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren&#39;t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you&#39;re Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it&#39;s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let&#39;s do more of those!
</code></pre>

<h3>Pycodestyle</h3>

<p><code>Pycodestyle</code> is now the <a href="/rltoken/D67mmHg2X9ZI7QHlQxayyw" title="new standard of Python style code" target="_blank">new standard of Python style code</a></p>

<p><br />
<br />
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/Flyingcircus_2.jpg" alt="" style="" /></p>

</div>


      

        <h2 class="gap" id="project-quiz-questions-title">
    Quiz questions
  </h2>


  <div class="panel panel-default">
    <div class="panel-body">
        <div class="alert alert-info">
          <strong>Great!</strong>
          You've completed the quiz successfully! Keep going!
          <span id="quiz_questions_collapse_toggle"></span>
        </div>

      <section class="quiz_questions_show_container">
          <div class="quiz_question_item_container" data-role="quiz_question206" data-position="1">
            <div class=" clearfix" id="quiz_question-206">

    <h4 class="quiz_question">
        
        Question #0
    </h4>

    <!-- Quiz question Body -->
    <p>Who created Python?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="206">
                <li class="">
  <input type="checkbox" name="quiz-answer-1501118951332" id="quiz-answer-1501118951332" data-quiz-question-id="206" data-quiz-answer-id="1501118951332" disabled="disabled" />
  <label for="quiz-answer-1501118951332">
    <p>Julien Barbier</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501118958787" id="quiz-answer-1501118958787" data-quiz-question-id="206" data-quiz-answer-id="1501118958787" disabled="disabled" />
  <label for="quiz-answer-1501118958787">
    <p>Yukihiro Matsumoto</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119040391" id="quiz-answer-1501119040391" data-quiz-question-id="206" data-quiz-answer-id="1501119040391" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1501119040391">
    <p>Guido van Rossum</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question207" data-position="2">
            <div class=" clearfix" id="quiz_question-207">

    <h4 class="quiz_question">
        
        Question #1
    </h4>

    <!-- Quiz question Body -->
    <p>What does this command line print?</p>

<pre><code>&gt;&gt;&gt; print(&quot;Holberton school&quot;)
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="207">
                <li class="">
  <input type="checkbox" name="quiz-answer-1501119054589" id="quiz-answer-1501119054589" data-quiz-question-id="207" data-quiz-answer-id="1501119054589" disabled="disabled" />
  <label for="quiz-answer-1501119054589">
    <p>Holberton</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119061010" id="quiz-answer-1501119061010" data-quiz-question-id="207" data-quiz-answer-id="1501119061010" disabled="disabled" />
  <label for="quiz-answer-1501119061010">
    <p>&ldquo;Holberton school&rdquo;</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119064212" id="quiz-answer-1501119064212" data-quiz-question-id="207" data-quiz-answer-id="1501119064212" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1501119064212">
    <p>Holberton school</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119077323" id="quiz-answer-1501119077323" data-quiz-question-id="207" data-quiz-answer-id="1501119077323" disabled="disabled" />
  <label for="quiz-answer-1501119077323">
    <p>&lsquo;Holberton school&rsquo;</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question208" data-position="3">
            <div class=" clearfix" id="quiz_question-208">

    <h4 class="quiz_question">
        
        Question #2
    </h4>

    <!-- Quiz question Body -->
    <p>What does this command line print?</p>

<pre><code>&gt;&gt;&gt; print(&quot;{:d} Battery street&quot;.format(98))
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="208">
                <li class="">
  <input type="checkbox" name="quiz-answer-1501119088766" id="quiz-answer-1501119088766" data-quiz-question-id="208" data-quiz-answer-id="1501119088766" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1501119088766">
    <p>98 Battery street</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119091386" id="quiz-answer-1501119091386" data-quiz-question-id="208" data-quiz-answer-id="1501119091386" disabled="disabled" />
  <label for="quiz-answer-1501119091386">
    <p>&ldquo;98 Battery street&rdquo;</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119094887" id="quiz-answer-1501119094887" data-quiz-question-id="208" data-quiz-answer-id="1501119094887" disabled="disabled" />
  <label for="quiz-answer-1501119094887">
    <p>9 Battery street</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119099084" id="quiz-answer-1501119099084" data-quiz-question-id="208" data-quiz-answer-id="1501119099084" disabled="disabled" />
  <label for="quiz-answer-1501119099084">
    <p>8 Battery street</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question209" data-position="4">
            <div class=" clearfix" id="quiz_question-209">

    <h4 class="quiz_question">
        
        Question #3
    </h4>

    <!-- Quiz question Body -->
    <p>What does this command line print?</p>

<pre><code>&gt;&gt;&gt; print(&quot;{:d} Battery street, {}&quot;.format(98, &quot;San Francisco&quot;))
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="209">
                <li class="">
  <input type="checkbox" name="quiz-answer-1501119111068" id="quiz-answer-1501119111068" data-quiz-question-id="209" data-quiz-answer-id="1501119111068" disabled="disabled" />
  <label for="quiz-answer-1501119111068">
    <p>&ldquo;98 Battery street, San Francisco&rdquo;</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119114029" id="quiz-answer-1501119114029" data-quiz-question-id="209" data-quiz-answer-id="1501119114029" disabled="disabled" />
  <label for="quiz-answer-1501119114029">
    <p>8 Battery street, San</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119121729" id="quiz-answer-1501119121729" data-quiz-question-id="209" data-quiz-answer-id="1501119121729" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1501119121729">
    <p>98 Battery street, San Francisco</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119127898" id="quiz-answer-1501119127898" data-quiz-question-id="209" data-quiz-answer-id="1501119127898" disabled="disabled" />
  <label for="quiz-answer-1501119127898">
    <p>San Francisco Battery street, 98</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question210" data-position="5">
            <div class=" clearfix" id="quiz_question-210">

    <h4 class="quiz_question">
        
        Question #4
    </h4>

    <!-- Quiz question Body -->
    <p>What does this command line print?</p>

<pre><code>&gt;&gt;&gt; a = &quot;Python is cool&quot;
&gt;&gt;&gt; print(a[4])
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="210">
                <li class="">
  <input type="checkbox" name="quiz-answer-1501119139787" id="quiz-answer-1501119139787" data-quiz-question-id="210" data-quiz-answer-id="1501119139787" disabled="disabled" />
  <label for="quiz-answer-1501119139787">
    <p>P</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119144377" id="quiz-answer-1501119144377" data-quiz-question-id="210" data-quiz-answer-id="1501119144377" disabled="disabled" />
  <label for="quiz-answer-1501119144377">
    <p>n</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119148659" id="quiz-answer-1501119148659" data-quiz-question-id="210" data-quiz-answer-id="1501119148659" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1501119148659">
    <p>o</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119156164" id="quiz-answer-1501119156164" data-quiz-question-id="210" data-quiz-answer-id="1501119156164" disabled="disabled" />
  <label for="quiz-answer-1501119156164">
    <p>h</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question211" data-position="6">
            <div class=" clearfix" id="quiz_question-211">

    <h4 class="quiz_question">
        
        Question #5
    </h4>

    <!-- Quiz question Body -->
    <p>What does this command line print?</p>

<pre><code>&gt;&gt;&gt; a = &quot;Python is cool&quot;
&gt;&gt;&gt; print(a[0:6])
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="211">
                <li class="">
  <input type="checkbox" name="quiz-answer-1501119166146" id="quiz-answer-1501119166146" data-quiz-question-id="211" data-quiz-answer-id="1501119166146" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1501119166146">
    <p>Python</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119168793" id="quiz-answer-1501119168793" data-quiz-question-id="211" data-quiz-answer-id="1501119168793" disabled="disabled" />
  <label for="quiz-answer-1501119168793">
    <p>Pytho</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119171554" id="quiz-answer-1501119171554" data-quiz-question-id="211" data-quiz-answer-id="1501119171554" disabled="disabled" />
  <label for="quiz-answer-1501119171554">
    <p>Python is</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119205643" id="quiz-answer-1501119205643" data-quiz-question-id="211" data-quiz-answer-id="1501119205643" disabled="disabled" />
  <label for="quiz-answer-1501119205643">
    <p>Python is cool</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question212" data-position="7">
            <div class=" clearfix" id="quiz_question-212">

    <h4 class="quiz_question">
        
        Question #6
    </h4>

    <!-- Quiz question Body -->
    <p>What does this command line print?</p>

<pre><code>&gt;&gt;&gt; a = &quot;Python is cool&quot;
&gt;&gt;&gt; print(a[:6])
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="212">
                <li class="">
  <input type="checkbox" name="quiz-answer-1501119213915" id="quiz-answer-1501119213915" data-quiz-question-id="212" data-quiz-answer-id="1501119213915" disabled="disabled" />
  <label for="quiz-answer-1501119213915">
    <p>Pytho</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119221132" id="quiz-answer-1501119221132" data-quiz-question-id="212" data-quiz-answer-id="1501119221132" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1501119221132">
    <p>Python</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119226331" id="quiz-answer-1501119226331" data-quiz-question-id="212" data-quiz-answer-id="1501119226331" disabled="disabled" />
  <label for="quiz-answer-1501119226331">
    <p>Python is</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119229193" id="quiz-answer-1501119229193" data-quiz-question-id="212" data-quiz-answer-id="1501119229193" disabled="disabled" />
  <label for="quiz-answer-1501119229193">
    <p>is cool</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question213" data-position="8">
            <div class=" clearfix" id="quiz_question-213">

    <h4 class="quiz_question">
        
        Question #7
    </h4>

    <!-- Quiz question Body -->
    <p>What does this command line print?</p>

<pre><code>&gt;&gt;&gt; a = &quot;Python is cool&quot;
&gt;&gt;&gt; print(a[7:])
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="213">
                <li class="">
  <input type="checkbox" name="quiz-answer-1501119240782" id="quiz-answer-1501119240782" data-quiz-question-id="213" data-quiz-answer-id="1501119240782" disabled="disabled" />
  <label for="quiz-answer-1501119240782">
    <p>Python i</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119245842" id="quiz-answer-1501119245842" data-quiz-question-id="213" data-quiz-answer-id="1501119245842" disabled="disabled" />
  <label for="quiz-answer-1501119245842">
    <p>Python is</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119249907" id="quiz-answer-1501119249907" data-quiz-question-id="213" data-quiz-answer-id="1501119249907" disabled="disabled" />
  <label for="quiz-answer-1501119249907">
    <p>cool</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119252189" id="quiz-answer-1501119252189" data-quiz-question-id="213" data-quiz-answer-id="1501119252189" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1501119252189">
    <p>is cool</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question214" data-position="9">
            <div class=" clearfix" id="quiz_question-214">

    <h4 class="quiz_question">
        
        Question #8
    </h4>

    <!-- Quiz question Body -->
    <p>What does this command line print?</p>

<pre><code>&gt;&gt;&gt; a = &quot;Python is cool&quot;
&gt;&gt;&gt; print(a[7:-5])
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="214">
                <li class="">
  <input type="checkbox" name="quiz-answer-1501119260641" id="quiz-answer-1501119260641" data-quiz-question-id="214" data-quiz-answer-id="1501119260641" disabled="disabled" />
  <label for="quiz-answer-1501119260641">
    <p>on</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119264681" id="quiz-answer-1501119264681" data-quiz-question-id="214" data-quiz-answer-id="1501119264681" disabled="disabled" />
  <label for="quiz-answer-1501119264681">
    <p>nohtyP</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119275621" id="quiz-answer-1501119275621" data-quiz-question-id="214" data-quiz-answer-id="1501119275621" disabled="disabled" />
  <label for="quiz-answer-1501119275621">
    <p>Python</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119283007" id="quiz-answer-1501119283007" data-quiz-question-id="214" data-quiz-answer-id="1501119283007" disabled="disabled" />
  <label for="quiz-answer-1501119283007">
    <p>si</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119288237" id="quiz-answer-1501119288237" data-quiz-question-id="214" data-quiz-answer-id="1501119288237" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1501119288237">
    <p>is</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question215" data-position="10">
            <div class=" clearfix" id="quiz_question-215">

    <h4 class="quiz_question">
        
        Question #9
    </h4>

    <!-- Quiz question Body -->
    <p>What does this command line print?</p>

<pre><code>&gt;&gt;&gt; a = &quot;Python is cool&quot;
&gt;&gt;&gt; print(a[-2])
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="215">
                <li class="">
  <input type="checkbox" name="quiz-answer-1501119297417" id="quiz-answer-1501119297417" data-quiz-question-id="215" data-quiz-answer-id="1501119297417" disabled="disabled" />
  <label for="quiz-answer-1501119297417">
    <p>ol</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119304573" id="quiz-answer-1501119304573" data-quiz-question-id="215" data-quiz-answer-id="1501119304573" disabled="disabled" />
  <label for="quiz-answer-1501119304573">
    <p>l</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119307071" id="quiz-answer-1501119307071" data-quiz-question-id="215" data-quiz-answer-id="1501119307071" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1501119307071">
    <p>o</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1501119313121" id="quiz-answer-1501119313121" data-quiz-question-id="215" data-quiz-answer-id="1501119313121" disabled="disabled" />
  <label for="quiz-answer-1501119313121">
    <p>Nothing</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>

      </section>
    </div>
  </div>


        
          <h2 class="gap">Tasks</h2>

    <div data-role="task1007" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-1007">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Run Python file
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1007" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a Shell script that runs a Python script.</p>

<p>The Python file name will be saved in the environment variable <code>$PYFILE</code></p>

<pre><code>guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print(&quot;Best School&quot;)

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>0-run</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1007">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1007" data-project-id="231" data-toggle="modal" data-target="#task-1007-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1007-users-done-modal" data-task-id="1007" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "0. Run Python file"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1007" data-toggle="modal" data-target="#task-test-correction-1007-correction-modal" id="task-num-0-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1007-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "0. Run Python file"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1007">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1007">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1007">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1007" data-toggle="modal" data-target="#task-qa-review-1007-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1007-modal" data-correction-id="243739" data-task-id="1007">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">0. Run Python file</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1012" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-1012">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Run inline
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1012" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a Shell script that runs Python code.</p>

<p>The Python code will be saved in the environment variable <code>$PYCODE</code></p>

<pre><code>guillaume@ubuntu:~/py/0x00$ export PYCODE=&#39;print(&quot;Best School: {}&quot;.format(88+10))&#39;
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>1-run_inline</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1012">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1012" data-project-id="231" data-toggle="modal" data-target="#task-1012-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1012-users-done-modal" data-task-id="1012" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "1. Run inline"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1012" data-toggle="modal" data-target="#task-test-correction-1012-correction-modal" id="task-num-1-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1012-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "1. Run inline"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1012">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1012">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1012">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1012" data-toggle="modal" data-target="#task-qa-review-1012-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1012-modal" data-correction-id="243739" data-task-id="1012">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">1. Run inline</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1013" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-1013">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Hello, print
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1013" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a Python script that prints exactly <code>&quot;Programming is like building a multilingual puzzle</code>, followed by a new line.</p>

<ul>
<li>Use the function <code>print</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./2-print.py 
&quot;Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>2-print.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1013">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1013" data-project-id="231" data-toggle="modal" data-target="#task-1013-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1013-users-done-modal" data-task-id="1013" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "2. Hello, print"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1013" data-toggle="modal" data-target="#task-test-correction-1013-correction-modal" id="task-num-2-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1013-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "2. Hello, print"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1013">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1013">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1013">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1013" data-toggle="modal" data-target="#task-qa-review-1013-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1013-modal" data-correction-id="243739" data-task-id="1013">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">2. Hello, print</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1019" data-position="4" id="task-num-3">
      <div class="panel panel-default task-card " id="task-1019">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Print integer
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1019" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py" title="source code" target="_blank">source code</a> in order to print the integer stored in the variable <code>number</code>, followed by <code>Battery street</code>, followed by a new line.</p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py" title="here" target="_blank">here</a></li>
<li>The output of the script should be:

<ul>
<li>the number, followed by <code>Battery street</code>,</li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to cast the variable <code>number</code> into a string</li>
<li>Your code must be 3 lines long</li>
<li>You have to use the new print numbers <a href="/rltoken/k33L_JH5NMcE3c4LsUkVlA" title="tips" target="_blank">tips</a> (with <code>.format(...)</code>)</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

<blockquote>
<p>C is strongly typed&hellip; not in Python! The variable <code>number</code> can be assigned to a string, a float, a bool etc&hellip; Forcing the type during a string format (<code>&quot;...&quot;.format(...)</code>) is a way to control the type of a variable</p>
</blockquote>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>3-print_number.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1019">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1019" data-project-id="231" data-toggle="modal" data-target="#task-1019-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1019-users-done-modal" data-task-id="1019" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "3. Print integer"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1019" data-toggle="modal" data-target="#task-test-correction-1019-correction-modal" id="task-num-3-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1019-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "3. Print integer"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1019">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1019">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1019">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1019" data-toggle="modal" data-target="#task-qa-review-1019-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1019-modal" data-correction-id="243739" data-task-id="1019">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">3. Print integer</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1020" data-position="5" id="task-num-4">
      <div class="panel panel-default task-card " id="task-1020">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Print float
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1020" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Complete the source code in order to print the float stored in the variable <code>number</code> with a precision of 2 digits.</p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py" title="here" target="_blank">here</a></li>
<li>The output of the program should be:

<ul>
<li><code>Float:</code>, followed by the float with only 2 digits</li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to cast <code>number</code> to string</li>
<li>You have to use the new print formatting <a href="/rltoken/CLkyFheLlanPlBS4ySOg7A" title="tips" target="_blank">tips</a>  (with <code>.format(...)</code>)</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>4-print_float.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1020">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1020" data-project-id="231" data-toggle="modal" data-target="#task-1020-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1020-users-done-modal" data-task-id="1020" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "4. Print float"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1020" data-toggle="modal" data-target="#task-test-correction-1020-correction-modal" id="task-num-4-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1020-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "4. Print float"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1020">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1020">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1020">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1020" data-toggle="modal" data-target="#task-qa-review-1020-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1020-modal" data-correction-id="243739" data-task-id="1020">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">4. Print float</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1021" data-position="6" id="task-num-5">
      <div class="panel panel-default task-card " id="task-1021">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Print string
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1021" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py" title="source code" target="_blank">source code</a> in order to print 3 times a string stored in the variable <code>str</code>, followed by its first 9 characters.</p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py" title="here" target="_blank">here</a></li>
<li>The output of the program should be:

<ul>
<li>3 times the value of <code>str</code></li>
<li>followed by a new line</li>
<li>followed by the 9 first characters of <code>str</code></li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to use any loops or conditional statement</li>
<li>Your program should be maximum 5 lines long</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>5-print_string.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1021">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1021" data-project-id="231" data-toggle="modal" data-target="#task-1021-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1021-users-done-modal" data-task-id="1021" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "5. Print string"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1021" data-toggle="modal" data-target="#task-test-correction-1021-correction-modal" id="task-num-5-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1021-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "5. Print string"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1021">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1021">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1021">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1021" data-toggle="modal" data-target="#task-qa-review-1021-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1021-modal" data-correction-id="243739" data-task-id="1021">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">5. Print string</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1079" data-position="7" id="task-num-6">
      <div class="panel panel-default task-card " id="task-1079">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Play with strings
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1079" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py" title="source code" target="_blank">source code</a> to print <code>Welcome to Holberton School!</code></p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py" title="here" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements.</li>
<li>You have to use the variables <code>str1</code> and <code>str2</code> in your new line of code</li>
<li>Your program should be exactly 5 lines long</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>6-concat.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1079">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1079" data-project-id="231" data-toggle="modal" data-target="#task-1079-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1079-users-done-modal" data-task-id="1079" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "6. Play with strings"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1079" data-toggle="modal" data-target="#task-test-correction-1079-correction-modal" id="task-num-6-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1079-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "6. Play with strings"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1079">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1079">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1079">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1079" data-toggle="modal" data-target="#task-qa-review-1079-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1079-modal" data-correction-id="243739" data-task-id="1079">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">6. Play with strings</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1080" data-position="8" id="task-num-7">
      <div class="panel panel-default task-card " id="task-1080">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Copy - Cut - Paste
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1080" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py" title="source code" target="_blank">source code</a></p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py" title="here" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements</li>
<li>Your program should be exactly 8 lines long</li>
<li><code>word_first_3</code> should contain the first 3 letters of the variable <code>word</code></li>
<li><code>word_last_2</code> should contain the last 2 letters of the variable <code>word</code></li>
<li><code>middle_word</code> should contain the value of the variable <code>word</code> without the first and last letters</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>7-edges.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1080">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1080" data-project-id="231" data-toggle="modal" data-target="#task-1080-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1080-users-done-modal" data-task-id="1080" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "7. Copy - Cut - Paste"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1080" data-toggle="modal" data-target="#task-test-correction-1080-correction-modal" id="task-num-7-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1080-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "7. Copy - Cut - Paste"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1080">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1080">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1080">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1080" data-toggle="modal" data-target="#task-qa-review-1080-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1080-modal" data-correction-id="243739" data-task-id="1080">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">7. Copy - Cut - Paste</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1081" data-position="9" id="task-num-8">
      <div class="panel panel-default task-card " id="task-1081">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Create a new sentence
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1081" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Complete this <a href="https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py" title="source code" target="_blank">source code</a> to print <code>object-oriented programming with Python</code>, followed by a new line.</p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py" title="here" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements</li>
<li>Your program should be exactly 5 lines long</li>
<li>You are not allowed to create new variables</li>
<li>You are not allowed to use string literals</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>8-concat_edges.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1081">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1081" data-project-id="231" data-toggle="modal" data-target="#task-1081-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1081-users-done-modal" data-task-id="1081" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "8. Create a new sentence"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1081" data-toggle="modal" data-target="#task-test-correction-1081-correction-modal" id="task-num-8-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1081-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "8. Create a new sentence"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1081">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1081">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1081">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1081" data-toggle="modal" data-target="#task-qa-review-1081-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1081-modal" data-correction-id="243739" data-task-id="1081">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">8. Create a new sentence</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1082" data-position="10" id="task-num-9">
      <div class="panel panel-default task-card " id="task-1082">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. Easter Egg
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1082" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a Python script that prints &ldquo;The Zen of Python&rdquo;, by TimPeters, followed by a new line.</p>

<ul>
<li>Your script should be maximum 98 characters long (please check with <code>wc -m 9-easter_egg.py</code>)</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren&#39;t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you&#39;re Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it&#39;s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let&#39;s do more of those!
guillaume@ubuntu:~/py/0x00$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>9-easter_egg.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1082">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1082" data-project-id="231" data-toggle="modal" data-target="#task-1082-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1082-users-done-modal" data-task-id="1082" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "9. Easter Egg"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1082" data-toggle="modal" data-target="#task-test-correction-1082-correction-modal" id="task-num-9-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1082-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "9. Easter Egg"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1082">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1082">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1082">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1082" data-toggle="modal" data-target="#task-qa-review-1082-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1082-modal" data-correction-id="243739" data-task-id="1082">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">9. Easter Egg</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task2656" data-position="11" id="task-num-10">
      <div class="panel panel-default task-card " id="task-2656">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. Linked list cycle
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="2656" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
<li>This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution&rsquo;s runtime fast enough, does your solution require extra memory usage / mallocs, etc.</li>
</ul>

<p>Write a function in C that checks if a singly linked list has a cycle in it.</p>

<ul>
<li>Prototype: <code>int check_cycle(listint_t *list);</code></li>
<li>Return: <code>0</code> if there is no cycle, <code>1</code> if there is a cycle</li>
</ul>

<p>Requirements:</p>

<ul>
<li>Only these functions are allowed: <code>write</code>, <code>printf</code>, <code>putchar</code>, <code>puts</code>, <code>malloc</code>, <code>free</code></li>
</ul>

<pre><code>carrie@ubuntu:~/0x00$ cat lists.h
#ifndef LISTS_H
#define LISTS_H

#include &lt;stdlib.h&gt;

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
</code></pre>

<pre><code>carrie@ubuntu:~/0x00$ cat 10-linked_lists.c
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &quot;lists.h&quot;

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf(&quot;%i\n&quot;, current-&gt;n);
        current = current-&gt;next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new-&gt;n = n;
    new-&gt;next = *head;
    *head = new;

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head-&gt;next;
        free(current);
    }
}
</code></pre>

<pre><code>carrie@ubuntu:~/0x00$ cat 10-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include &quot;lists.h&quot;

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *current;
    listint_t *temp;
    int i;

    head = NULL;
    add_nodeint(&amp;head, 0);
    add_nodeint(&amp;head, 1);
    add_nodeint(&amp;head, 2);
    add_nodeint(&amp;head, 3);
    add_nodeint(&amp;head, 4);
    add_nodeint(&amp;head, 98);
    add_nodeint(&amp;head, 402);
    add_nodeint(&amp;head, 1024);
    print_listint(head);

    if (check_cycle(head) == 0)
        printf(&quot;Linked list has no cycle\n&quot;);
    else if (check_cycle(head) == 1)
        printf(&quot;Linked list has a cycle\n&quot;);

    current = head;
    for (i = 0; i &lt; 4; i++)
        current = current-&gt;next;
    temp = current-&gt;next;
    current-&gt;next = head;

    if (check_cycle(head) == 0)
        printf(&quot;Linked list has no cycle\n&quot;);
    else if (check_cycle(head) == 1)
        printf(&quot;Linked list has a cycle\n&quot;);

    current = head;
    for (i = 0; i &lt; 4; i++)
        current = current-&gt;next;
    current-&gt;next = temp;

    free_listint(head);

    return (0);
}
</code></pre>

<pre><code>carrie@ubuntu:~/0x00$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
carrie@ubuntu:~/0x00$$ ./cycle 
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
carrie@ubuntu:~/0x00$
</code></pre>

<blockquote>
<p>Solving a problem is already a big win! but finding the best and optimal way to solve it, it&rsquo;s way better! Think about the most optimal / fastest way to do it.</p>
</blockquote>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>10-check_cycle.c, lists.h</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="2656">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="2656" data-project-id="231" data-toggle="modal" data-target="#task-2656-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-2656-users-done-modal" data-task-id="2656" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "10. Linked list cycle"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="2656" data-toggle="modal" data-target="#task-test-correction-2656-correction-modal" id="task-num-10-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-2656-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "10. Linked list cycle"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="2656">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="2656">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="2656">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


      <button class="btn btn-primary btn-sm task_ask_new_correction" data-task-id="2656" data-correction-id="243739">
        Ask for a new correction <span class="in_progress_info">: in progress...</span><span class="error_occured_info">: an error occured</span>
      </button>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="2656" data-toggle="modal" data-target="#task-qa-review-2656-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-2656-modal" data-correction-id="243739" data-task-id="2656">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">10. Linked list cycle</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1014" data-position="100" id="task-num-11">
      <div class="panel panel-default task-card " id="task-1014">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      11. Hello, write
    </h3>

    <div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1014" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a Python script that prints exactly <code>and that piece of art is useful - Dora Korpar, 2015-10-19</code>, followed by a new line.</p>

<ul>
<li>Use the function <code>write</code> from the <code>sys</code> module</li>
<li>You are not allowed to use <code>print</code></li>
<li>Your script should print to <code>stderr</code></li>
<li>Your script should exit with the status code <code>1</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2&gt; q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>100-write.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1014">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1014" data-project-id="231" data-toggle="modal" data-target="#task-1014-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1014-users-done-modal" data-task-id="1014" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "11. Hello, write"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1014" data-toggle="modal" data-target="#task-test-correction-1014-correction-modal" id="task-num-11-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1014-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "11. Hello, write"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1014">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1014">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1014">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1014" data-toggle="modal" data-target="#task-qa-review-1014-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1014-modal" data-correction-id="243739" data-task-id="1014">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">11. Hello, write</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1010" data-position="101" id="task-num-12">
      <div class="panel panel-default task-card " id="task-1010">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      12. Compile
    </h3>

    <div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1010" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a script that compiles a Python script file.</p>

<p>The Python file name will be stored in the environment variable <code>$PYFILE</code></p>

<p>The output filename has to be <code>$PYFILEc</code> (ex: <code>export PYFILE=my_main.py</code> =&gt; output filename: <code>my_main.pyc</code>)</p>

<pre><code>guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print(&quot;Best School&quot;)

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./101-compile
Compiling main.py ...
guillaume@ubuntu:~/py/0x00$ ls
101-compile  main.py  main.pyc
guillaume@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c &quot;Best School&quot;
1
guillaume@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT =&gt; CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>101-compile</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1010">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1010" data-project-id="231" data-toggle="modal" data-target="#task-1010-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1010-users-done-modal" data-task-id="1010" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "12. Compile"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1010" data-toggle="modal" data-target="#task-test-correction-1010-correction-modal" id="task-num-12-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1010-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "12. Compile"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1010">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1010">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1010">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1010" data-toggle="modal" data-target="#task-qa-review-1010-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1010-modal" data-correction-id="243739" data-task-id="1010">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">12. Compile</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>
    <div data-role="task1025" data-position="102" id="task-num-13">
      <div class="panel panel-default task-card " id="task-1025">
  <span id="user_id" data-id="3400"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      13. ByteCode -&gt; Python #1
    </h3>

    <div>
        <span class="label label-info">
          #advanced
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="3400"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1025" data-correction-id="243739">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write the Python function <code>def magic_calculation(a, b):</code> that does exactly the same as the following Python bytecode:</p>

<pre><code>  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
</code></pre>

<ul>
<li>Tip: <a href="/rltoken/FYK4MePotTrqXCfiKYxL7Q" title="Python bytecode" target="_blank">Python bytecode</a></li>
</ul>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x00-python-hello_world</code></li>
            <li>File: <code>102-magic_calculation.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1025">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1025" data-project-id="231" data-toggle="modal" data-target="#task-1025-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1025-users-done-modal" data-task-id="1025" data-project-id="231">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "13. ByteCode -&gt; Python #1"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm" data-task-id="1025" data-toggle="modal" data-target="#task-test-correction-1025-correction-modal" id="task-num-13-check-code-btn">
        Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1025-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "13. ByteCode -&gt; Python #1"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1025">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="pre-check-message">
                                <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                                    <img src="/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png" />
                                </a>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <a href="https://twitter.com/hashtag/HbtnWomensHistoryMonth" target="_blank">
                            <img src="/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png" />
                        </a>
                    </div>

                <div class="help">
    <button data-task-id="1025">
        <i aria-hidden="true" class="fa fa-info-circle "></i>
    </button>
    <div class="help-container" data-task-id="1025">
        <div class="check-line">
            <div class="check-inline requirement success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                  <i aria-hidden="true" class="fa fa-check-circle "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                  <i aria-hidden="true" class="fa fa-times-circle "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1025" data-toggle="modal" data-target="#task-qa-review-1025-modal">
        QA Review
      </button>
      <div class="modal fade task_get_qa_review" id="task-qa-review-1025-modal" data-correction-id="243739" data-task-id="1025">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">13. ByteCode -&gt; Python #1</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github well" style="display:none">
                        <h5>Commit used:</h5>
                        <ul>
                            <li style="display:none"><strong>User:</strong> <code class="review-github-id"></code> <span class="review-github-name">---</span></li>
                            <li style="display:none"><strong>URL:</strong> <a class="review-github-url" target="_blank">Click here</a></li>
                            <li style="display:none"><strong>ID:</strong> <code class="review-github-commit_id">---</code></li>
                            <li style="display:none"><strong>Author:</strong> <span class="review-github-committer_username">---</span></li>
                            <li style="display:none"><strong>Subject:</strong> <em class="review-github-subject">---</em></li>
                            <li style="display:none"><strong>Date:</strong> <span class="review-github-datetime">---</span></li>
                        </ul>
                    </div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

    </div>


</div>

    </div>





          <div class="modal fade" id="container-specs-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandbox</h4></div><div class="modal-body"><div data-react-class="user_containers/ContainerSpecs" data-react-props="{&quot;containerModelName&quot;:&quot;Sandbox&quot;,&quot;containerSpecs&quot;:[{&quot;description&quot;:&quot;\u003cp\u003eBasic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations\u003c/p\u003e\n&quot;,&quot;id&quot;:39,&quot;name&quot;:&quot;Ubuntu 20.04&quot;,&quot;online&quot;:true,&quot;container&quot;:{&quot;containerId&quot;:&quot;a35827e28577a5106dd361365f22ba14c51679824a7c935c80c424a05b8e3d8f&quot;,&quot;host&quot;:&quot;a35827e28577.2410e53b.hbtn-cod.io&quot;,&quot;id&quot;:20499,&quot;password&quot;:&quot;be6234721b7df8723ffd&quot;,&quot;ports&quot;:{&quot;3306&quot;:49239,&quot;4000&quot;:49238,&quot;443&quot;:49241,&quot;5001&quot;:49236,&quot;8000&quot;:49235,&quot;8080&quot;:49234,&quot;22&quot;:49243,&quot;3000&quot;:49240,&quot;5000&quot;:49237,&quot;80&quot;:49242},&quot;url&quot;:&quot;/user_containers/20499.json&quot;,&quot;webtermUrl&quot;:&quot;/user_containers/20499/webterm&quot;}}],&quot;containersLimit&quot;:5,&quot;csrfToken&quot;:&quot;uTUP1ANSztBdohWIy2WrFwBDwNDeMC60uYi+1MWX8Q72T9E90B378jqyds2MbIuYfkO/aqZ2x2X3+A0AHpj+NQ==&quot;,&quot;startURI&quot;:&quot;/user_containers/start.json&quot;}" data-react-cache-id="user_containers/ContainerSpecs-0"></div></div></div></div></div>


  </div>
</div>


      </article>

      <div class="copyright">Copyright © 2022 Holberton Inc, All rights reserved.</div>
    </main>

      <button class="btn btn-primary" id="search-button" data-search-active="false" data-toggle="modal" data-target="#search-modal">
  <i aria-hidden="true" class="fa fa-search "></i>
  <i aria-hidden="true" class="fa fa-window-minimize "></i>
</button>

      <div class="modal fade" id="search-modal" tabindex="-1" role="dialog" aria-labelledby="search-modal-label">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <div id="search-bar-container">
    <input id="search-bar"
            type="text"
            name="hbtn-search-bar"
            placeholder="✨Start search by typing in this field✨">
</div>

            </div>
            <div class="modal-body">
                <div id="modal-spinner" class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div id="search-results-container">
</div>

            </div>
        </div>
    </div>
</div>



      <div class="modal fade" id="markdownGuideModal" tabindex="-1" role="dialog" aria-labelledby="markdownGuideModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-md">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title">Markdown Guide</h4>
        </div>
        <div class="modal-body">
            <h4>Emphasis</h4>
<pre>**<strong>bold</strong>**
*<em>italics</em>*
~~<strike>strikethrough</strike>~~</pre>
<h4>Headers</h4>
<pre># Big header
## Medium header
### Small header
#### Tiny header</pre>
<h4>Lists</h4>
<pre>* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item</pre>
<h4>Links</h4>
<pre>[Text to display](http://www.example.com)</pre>
<h4>Quotes</h4>
<pre>> This is a quote.
> It can span multiple lines!</pre>
<h4>Images</h4>
<p>CSS style available: <code>width, height, opacity</code></p>
<pre>![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
</pre>
<h4>Tables</h4>
<pre>| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
</pre>
<h4>Displaying code</h4>
<pre>`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```</pre>
        </div>
    </div>
  </div>
</div>


      <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

          ga('create',
            'UA-67152800-6',
            'auto', {
              userId: '3400'
            }
          );

        ga('send', 'pageview');

        $(document).ready(function() {
          ga(function(tracker) {
            var clientId = tracker.get('clientId');
            $('.ga-client-id').val(clientId);
          });
        });
      </script>




      


  </body>
</html>

