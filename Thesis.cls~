\ProvidesClass{Thesis}
\DeclareOption{PhD}{\def\degreetitle{Doctor of Philosophy}}
\DeclareOption{MSc}{\def\degreetitle{Master of Science}}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ExecuteOptions{PhD}
\ProcessOptions
\LoadClass[a4paper]{report}

%% Manchester University PhD thesis style -- modifications to the report style

%% We need >15mm  margins except on the binding edge, where it is >40mm
\oddsidemargin 14.6truemm \evensidemargin 0truemm
\marginparwidth 40pt \marginparsep 10pt
\topmargin 0truemm \headsep 10truemm
\textheight 224truemm \textwidth 145truemm


%% Disallow page breaks at hyphens (this will give some underfull vbox's,
%% so an alternative is to use \brokenpenalty=100 and manually search
%% for and fix such page breaks)
\brokenpenalty=10000

%% Use 1.6 times the normal baseline-to-baseline skip (approx double space)
\renewcommand{\baselinestretch}{1.6}

\renewcommand{\bottomfraction}{0.7}
\setlength{\floatsep}{10pt plus 2pt minus 2pt}
%% Redefine the macro used for floats (including figures and tables)
%% so that single spacing is used.
%% (Note \def\figure{\@float{figure}set single spacing} doesn't work
%%  because figure has an optional argument)
\def\@xfloat#1[#2]{\ifhmode \@bsphack\@floatpenalty -\@Mii\else
   \@floatpenalty-\@Miii\fi\def\@captype{#1}\ifinner
      \@parmoderr\@floatpenalty\z@
    \else\@next\@currbox\@freelist{\@tempcnta\csname ftype@#1\endcsname
       \multiply\@tempcnta\@xxxii\advance\@tempcnta\sixt@@n
       \@tfor \@tempa :=#2\do
                        {\if\@tempa h\advance\@tempcnta \@ne\fi
                         \if\@tempa t\advance\@tempcnta \tw@\fi
                         \if\@tempa b\advance\@tempcnta 4\relax\fi
                         \if\@tempa p\advance\@tempcnta 8\relax\fi
         }\global\count\@currbox\@tempcnta}\@fltovf\fi
    \global\setbox\@currbox\vbox\bgroup 
    \def\baselinestretch{1}\@normalsize
    \boxmaxdepth\z@
    \hsize\columnwidth \@parboxrestore}

%% Redefine the macro used for footnotes to use single spacing
\long\def\@footnotetext#1{\insert\footins{\def\baselinestretch{1}\footnotesize
    \interlinepenalty\interfootnotelinepenalty 
    \splittopskip\footnotesep
    \splitmaxdepth \dp\strutbox \floatingpenalty \@MM
    \hsize\columnwidth \@parboxrestore
   \edef\@currentlabel{\csname p@footnote\endcsname\@thefnmark}\@makefntext
    {\rule{\z@}{\footnotesep}\ignorespaces
      #1\strut}}}

%% \author, \title are defined in report; here are the rest of the
%% front matter defining macros
%% Note: If you really want, you can define your own macro for, say
%% \supervisor , just by copying the definitions of \principaladvisor
%%
\def\dept#1{\gdef\@dept{#1}}
\def\principaladviser#1{\gdef\@principaladviser{#1}}
\def\advis@r{Advisor} % default spelling---we are English!
%% Obviously, we could add a \supervisor macro
\def\principaladvisor#1{\gdef\@principaladviser{#1}\gdef\advis@r{Advisor}}
\def\firstreader#1{\gdef\@firstreader{#1}}
\def\secondreader#1{\gdef\@secondreader{#1}}
\def\submitdate#1{\gdef\@submitdate{#1}}
\def\copyrightyear#1{\gdef\@copyrightyear{#1}} % \author, \title in report
\def\@title{}\def\@author{}\def\@dept{Radio Astronomy}
\def\@principaladviser{}\def\@firstreader{}\def\@secondreader{}
%% only year of submission not month!
\def\@submitdate{\number\the\year}
%\def\@submitdate{\ifcase\the\month\or
%  January\or February\or March\or April\or May\or June\or
%  July\or August\or September\or October\or November\or December\fi
%  \space \number\the\year}
%% Stanford says that December theses should have the next year as the
%% copyright year
\ifnum\month=12
    \@tempcnta=\year \advance\@tempcnta by 1
    \edef\@copyrightyear{\number\the\@tempcnta}
\else
    \def\@copyrightyear{\number\the\year}
\fi
\newif\ifcopyright \newif\iffigurespage \newif\iftablespage \newif\ifsigpage
\copyrighttrue \figurespagetrue \tablespagetrue \sigpagefalse

%% If you're doing an MSc, I'm sure you can guess which parts to change
%% below; if not then you shouldn't be doing one.
\def\titlepagefont{
  \usefont{T1}{ppl}{b}{n}
}

\def\titlep{
\thispagestyle{empty}
  \begin{center}
    %\vspace[*]{2cm}
    %\vfill
    {\bf\huge\titlepagefont{\@title}}
    \vfill
    \vspace{4cm}
    {A thesis submitted to the University of Manchester for the degree of\\
      \degreetitle\\
      in the Faculty of Engineering and Physical Sciences}
    \vspace{3cm}
    \vfill
    \Large{\@submitdate}\\
    \vspace{4cm}
    \vfill
    \large{\@author} \\
    \vspace{1cm}
    \large\expandafter{\@dept}
  \end{center}
}

\def\declpage{
  \prefacesection{Declaration}

No portion of the work referred to in this thesis has been submitted in support of an application for another degree or qualification of this or any other university or other institution of learning.

\vspace*{2.5cm}
\noindent Gareth John Ashley Brown\\
School of Physics and Astronomy\\
University of Manchester\\
Oxford Road\\
Manchester\\
M13 9PL\\
November 2012\\
}

\def\copyrightpage{
  \prefacesection{Copyright}

  Copyright in text of this thesis rests with the Author. Copies (by any process) either in full, or of extracts, may be made {\bf only} in accordance with instructions given by the Author and lodged in the John Rylands University Library of Manchester. Details may be obtained from the Librarian. This page must form part of any such copies made. Further copies (by any process) of copies made in accordance with such instructions may not be made without the permission (in writing) of the Author.

  The ownership of any intellectual property rights which may be described in this thesis is vested in The University of Manchester, subject to any prior agreement to the contrary, and may not be made available for use by third parties without the written permission of the University, which will prescribe the terms and conditions of any such agreement.

  Further information on the conditions under which disclosures and exploitation may take place is available from the Head of the School of Physics and Astronomy.
  \vfill\newpage
}

\def\beforeabstract{
  \pagenumbering{arabic}
  \pagestyle{plain}
  \titlep
  \newpage
  \tableofcontents
  \begin{center}
    {\it Total word count: not yet set}
  \end{center}
  \newpage
  \iftablespage
     \listoftables
     \newpage
  \fi
  \iffigurespage
    \listoffigures
    \newpage
  \fi
}

\def\afterabstract{
  \newpage
  \declpage
  \copyrightpage
}

\def\prefacesection#1{
  \chapter*{#1}
  \addcontentsline{toc}{chapter}{#1}
}

\def\afterpreface{
  \newpage
  %\pagestyle{headings}
}

\pagestyle{plain}

\def\thebibliography#1{\chapter*{\bibname\@mkboth
  {\uppercase{\bibname}}{\uppercase{\bibname}}}
  \addcontentsline{toc}{chapter}{\bibname}
  \list
  {\@biblabel{\arabic{enumiv}}}{\settowidth\labelwidth{\@biblabel{#1}}
    \leftmargin\labelwidth
    \advance\leftmargin\labelsep
    \usecounter{enumiv}
    \let\p@enumiv\@empty
    \def\theenumiv{\arabic{enumiv}}}
    \def\newblock{\hskip .11em plus.33em minus.07em}
    \sloppy\clubpenalty4000\widowpenalty4000
    \sfcode`\.=\@m}

\def\endthebibliography{
  \def\@noitemerr{\@warning{Empty `thebibliography' environment}}
  \endlist}

\newif\if@cont
\def\caption{\refstepcounter\@captype \@dblarg{\@caption\@captype}}
\def\contcaption{\@conttrue\SFB@caption\@captype}
\long\def\SFB@caption#1#2{
 \begingroup
  \@parboxrestore
  \reset@font\normalsize
  \@makecaption{\csname fnum@#1\endcsname}{\ignorespaces #2}\par
 \endgroup}
