% businessdocs.cls - Master LaTeX class for business documentation suite
% UK English spelling throughout
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{businessdocs}[2024/01/01 Business Documentation Class]

% Base class
\LoadClass[11pt,a4paper,twoside]{article}

% Required packages
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage[UKenglish]{babel}
\RequirePackage[UKenglish]{isodate}
\RequirePackage{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{graphicx}
\RequirePackage{xcolor}
\RequirePackage{tikz}
\RequirePackage{pgfplots}
\RequirePackage{pgfgantt}
\RequirePackage{hyperref}
\RequirePackage{tocloft}
\RequirePackage{titlesec}
\RequirePackage{enumitem}
\RequirePackage{booktabs}
\RequirePackage{array}
\RequirePackage{multirow}
\RequirePackage{longtable}
\RequirePackage{float}
\RequirePackage{caption}
\RequirePackage{subcaption}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{siunitx}
\RequirePackage{eurosym}
\RequirePackage{lmodern}
\RequirePackage{microtype}
\RequirePackage[backend=biber,style=authoryear,citestyle=authoryear,natbib=true,sorting=nyt,maxbibnames=99]{biblatex}
\RequirePackage{csquotes}
\RequirePackage{cleveref}
\RequirePackage{glossaries}
\RequirePackage{makeidx}
\RequirePackage{listings}
\RequirePackage{tcolorbox}
\RequirePackage{mdframed}

% TikZ libraries
\usetikzlibrary{shapes,arrows,positioning,calc,patterns,decorations.pathreplacing,shadows,backgrounds}
\pgfplotsset{compat=1.18}

% Corporate colours
\definecolor{corporate-blue}{RGB}{0,48,87}
\definecolor{corporate-lightblue}{RGB}{70,130,180}
\definecolor{corporate-grey}{RGB}{128,128,128}
\definecolor{corporate-lightgrey}{RGB}{240,240,240}
\definecolor{accent-green}{RGB}{46,125,50}
\definecolor{accent-orange}{RGB}{255,152,0}
\definecolor{accent-red}{RGB}{198,40,40}

% Font configuration
% \setmainfont{Times New Roman}
% \setsansfont{Arial}
% \setmonofont{Courier New}

% Page geometry
\geometry{
    a4paper,
    left=25mm,
    right=25mm,
    top=30mm,
    bottom=30mm,
    headheight=15pt,
    headsep=10mm,
    footskip=15mm
}

% Header and footer styling
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\sffamily\small\thepage}
\fancyhead[RE]{\sffamily\small\leftmark}
\fancyhead[LO]{\sffamily\small\rightmark}
\fancyfoot[C]{\sffamily\footnotesize\@title}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.5pt}

% Section formatting
\titleformat{\section}
    {\normalfont\Large\bfseries\sffamily\color{corporate-blue}}
    {\thesection}{1em}{}
\titleformat{\subsection}
    {\normalfont\large\bfseries\sffamily\color{corporate-blue}}
    {\thesubsection}{1em}{}
\titleformat{\subsubsection}
    {\normalfont\normalsize\bfseries\sffamily\color{corporate-blue}}
    {\thesubsubsection}{1em}{}

% Table of contents styling
\renewcommand{\cftsecfont}{\sffamily\bfseries\color{corporate-blue}}
\renewcommand{\cftsubsecfont}{\sffamily\color{corporate-blue}}
\renewcommand{\cftsubsubsecfont}{\sffamily\color{corporate-grey}}

% Hyperref setup
\hypersetup{
    colorlinks=true,
    linkcolor=corporate-blue,
    citecolor=corporate-blue,
    urlcolor=corporate-lightblue,
    pdftitle={\@title},
    pdfauthor={\@author},
    bookmarks=true,
    bookmarksopen=true,
    bookmarksnumbered=true
}

% Custom commands
\newcommand{\companyname}{TechVenture Ltd}
\newcommand{\projectname}{Business Excellence Initiative}

% Financial formatting
\sisetup{
    group-separator={,},
    group-minimum-digits=3,
    detect-weight=true,
    detect-family=true
}
\newcommand{\poundsval}[1]{\pounds\num{#1}}
\newcommand{\euros}[1]{\euro\num{#1}}
\newcommand{\dollars}[1]{\$\num{#1}}

% Custom environments
\newenvironment{keypoint}{%
    \begin{tcolorbox}[
        colback=corporate-lightgrey,
        colframe=corporate-blue,
        boxrule=1pt,
        arc=3mm,
        left=5mm,
        right=5mm,
        top=5mm,
        bottom=5mm,
        fonttitle=\bfseries\sffamily,
        title=Key Point
    ]
}{\end{tcolorbox}}

\newenvironment{riskbox}{%
    \begin{tcolorbox}[
        colback=accent-red!10,
        colframe=accent-red,
        boxrule=1pt,
        arc=3mm,
        left=5mm,
        right=5mm,
        top=5mm,
        bottom=5mm,
        fonttitle=\bfseries\sffamily,
        title=Risk Assessment
    ]
}{\end{tcolorbox}}

\newenvironment{opportunitybox}{%
    \begin{tcolorbox}[
        colback=accent-green!10,
        colframe=accent-green,
        boxrule=1pt,
        arc=3mm,
        left=5mm,
        right=5mm,
        top=5mm,
        bottom=5mm,
        fonttitle=\bfseries\sffamily,
        title=Opportunity
    ]
}{\end{tcolorbox}}

% Milestone command for roadmaps
\newcommand{\milestone}[3]{%
    \node[draw=corporate-blue,fill=corporate-lightblue,circle,minimum size=8mm] at (#1,#2) {\bfseries\sffamily #3};
}

% SWOT analysis environment
\newenvironment{swotanalysis}{%
    \begin{tikzpicture}[remember picture,overlay]
        \def\swotwidth{0.45\textwidth}
        \def\swotheight{0.35\textheight}
}{%
    \end{tikzpicture}
}

% Gantt chart styling
\ganttset{
    canvas/.style={draw=none},
    bar/.style={fill=corporate-blue},
    bar incomplete/.style={fill=corporate-lightgrey},
    group/.style={fill=corporate-lightblue},
    milestone/.style={fill=accent-orange},
    link/.style={->,thick,corporate-blue}
}

% Title page command
\renewcommand{\maketitle}{%
    \begin{titlepage}
        \centering
        \vspace*{2cm}
        {\Huge\bfseries\sffamily\color{corporate-blue}\@title\par}
        \vspace{1.5cm}
        {\Large\sffamily\@author\par}
        \vspace{1cm}
        {\large\sffamily\@date\par}
        \vfill
        \begin{tikzpicture}
            \node[rectangle,draw=corporate-blue,line width=2pt,minimum width=0.8\textwidth,minimum height=3cm,align=center] {
                \Large\sffamily\companyname\\[0.5em]
                \large\projectname
            };
        \end{tikzpicture}
        \vfill
    \end{titlepage}
}

% Executive summary environment
\newenvironment{executivesummary}{%
    \section*{Executive Summary}
    \addcontentsline{toc}{section}{Executive Summary}
    \begin{mdframed}[
        linecolor=corporate-blue,
        linewidth=1pt,
        backgroundcolor=corporate-lightgrey!20,
        skipabove=10pt,
        skipbelow=10pt,
        innertopmargin=10pt,
        innerbottommargin=10pt
    ]
}{\end{mdframed}}

% KPI display command
\newcommand{\kpi}[3]{%
    \begin{tikzpicture}
        \node[rectangle,draw=corporate-blue,fill=corporate-lightgrey,minimum width=3cm,minimum height=2cm,align=center] {
            {\small\sffamily #1}\\[0.3em]
            {\Large\bfseries\sffamily #2}\\[0.2em]
            {\footnotesize\sffamily #3}
        };
    \end{tikzpicture}
}

% Cross-reference formatting
\crefname{section}{Section}{Sections}
\crefname{subsection}{Subsection}{Subsections}
\crefname{figure}{Figure}{Figures}
\crefname{table}{Table}{Tables}
\crefname{equation}{Equation}{Equations}

\endinput