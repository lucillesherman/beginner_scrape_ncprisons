# Scraping North Carolina's Prison [Covid-19 Case Counts](https://opus.doc.state.nc.us/DOPCovid19Stats/services/facilitystatsServlet)

1. Install [iTerm](https://iterm2.com/)<br>

2. Install [Chromedriver](https://chromedriver.chromium.org/downloads)<br>

3. Paste this in your terminal:
<pre><code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code></pre><br>
*Note: If you want to learn more about homebrew and what exactly it does (other than make your life incredibly easy, check it out [here](https://docs.brew.sh/Homebrew-and-Python).*<br>

4. Install python:
<pre><code>$ brew install python</code></pre><br>

5. Run:
	<pre><code>$ pip3 install virtualenv</code></pre>
	<pre><code>$ virtualenv state_prison_corona</code></pre>
	<pre><code>$ source state_prison_corona/bin/activate</code></pre>
	<pre><code>$ pip3 install -r requirements.txt</code></pre>


*Note: Once you're done working in your virtual environment, you can just simply run*
<pre><code>deactivate</code></pre>