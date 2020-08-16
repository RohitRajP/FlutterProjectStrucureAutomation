<h1 id="flutter-project-structure-creator">Flutter project structure creator</h1>
<p>This is an python based executable used to create a flutter project, and populate it with the file structure used by me for projects (following basic <a href="https://pub.dev/packages/provider">Provider</a> architecture) and also installs <a href="https://pub.dev/packages/effective_dart">effective dart</a> with the <code>analysis_options</code> file to manage the rules and their exceptions.</p>
<h2 id="project-structure">Project Structure</h2>
<h3 id="file-structure">File Structure</h3>
<p>The project file structure is split as :</p>
<ul>
<li><strong>global</strong>
<ul>
<li>Holds all the global:
<ul>
<li><strong>Widgets.</strong></li>
<li><strong>Controllers.</strong></li>
<li><strong>Scaffold Keys.</strong></li>
<li><strong>Theme Data.</strong></li>
<li><strong>Functions.</strong></li>
<li>&amp; <strong>Data Variables.</strong></li>
</ul>
</li>
<li>These objects can be accessed throughout the application, and are used to achieve code redundancy.</li>
</ul>
</li>
<li><strong>models</strong>
<ul>
<li>Holds the data models for state information to be used as per Provider state management strategy.</li>
<li>Each page has it’s own data model, through which both state and data flow throughout the application can be managed.</li>
</ul>
</li>
</ul>
<ul>
<li><strong>pages</strong>
<ul>
<li>Holds all the pages for the application. Each page is contained in a directory which is composed of:
<ul>
<li><strong>page_name.dart</strong> - holds the main scaffold for the page.</li>
<li><strong>widgets.dart</strong> - holds the widgets used by the page.</li>
<li><strong>functions.dart</strong> - holds the functional executing logic for the page.</li>
</ul>
</li>
</ul>
</li>
<li><strong>services</strong>
<ul>
<li>Holds all the functional code for all the in-app services.</li>
<li>For example:
<ul>
<li><strong>NetworkOps</strong> - API calls and other network operations.</li>
<li><strong>SharedPrefsOps</strong> - Local persistent storage operations.</li>
<li><strong>PermissionOps</strong> - Permission management operations.</li>
<li><strong>LocationOps</strong> - Maps and Location tracking operations.</li>
</ul>
</li>
</ul>
</li>
<li><strong>imports.dart</strong>
<ul>
<li>Used to export all libraries used commonly throughout the application.</li>
<li>Helps reduce the repeated importing of sample libraries of packages on multiple files.</li>
</ul>
</li>
</ul>
<h2 id="suggestions">Suggestions</h2>
<p>Any suggestions to my file structure are always welcome as I myself am trying to improve them as much as I can to suit all kinds of work loads.</p>
<p>Feel free to communicate:<br>
<a href="https://gitter.im/FlutterProjectStrucureAutomation/community?utm_source=badge&amp;utm_medium=badge&amp;utm_campaign=pr-badge&amp;utm_content=badge"><img src="https://badges.gitter.im/FlutterProjectStrucureAutomation/community.svg" alt="Gitter"></a></p>

