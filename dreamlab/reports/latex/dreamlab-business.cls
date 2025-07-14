% dreamlab-business.cls - LaTeX class for DreamLab AI Consulting business documentation
% Based on businessdocs.cls with DreamLab-specific customizations
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{dreamlab-business}[2025/01/11 DreamLab Business Documentation Class]

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
\RequirePackage{tabularx}
\RequirePackage{rotating}
\RequirePackage{pgf-pie}

% TikZ libraries
\usetikzlibrary{shapes,arrows,positioning,calc,patterns,decorations.pathreplacing,shadows,backgrounds,calendar}
\pgfplotsset{compat=1.18}

% DreamLab Corporate colours
\definecolor{dreamlab-purple}{RGB}{102,51,153}
\definecolor{dreamlab-blue}{RGB}{41,128,185}
\definecolor{dreamlab-lightblue}{RGB}{52,152,219}
\definecolor{dreamlab-green}{RGB}{39,174,96}
\definecolor{dreamlab-orange}{RGB}{243,156,18}
\definecolor{dreamlab-grey}{RGB}{127,140,141}
\definecolor{dreamlab-lightgrey}{RGB}{236,240,241}
\definecolor{dreamlab-dark}{RGB}{44,62,80}
\definecolor{dreamlab-lightgreen}{RGB}{169,223,191}
\definecolor{dreamlab-lightorange}{RGB}{243,178,122}
\definecolor{dreamlab-lightpurple}{RGB}{195,155,211}

% Font configuration
% Comment out custom fonts if not available
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
\fancyfoot[C]{\sffamily\footnotesize DreamLab AI Consulting - \@title}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.5pt}

% Section formatting
\titleformat{\section}
    {\normalfont\Large\bfseries\sffamily\color{dreamlab-purple}}
    {\thesection}{1em}{}
\titleformat{\subsection}
    {\normalfont\large\bfseries\sffamily\color{dreamlab-blue}}
    {\thesubsection}{1em}{}
\titleformat{\subsubsection}
    {\normalfont\normalsize\bfseries\sffamily\color{dreamlab-dark}}
    {\thesubsubsection}{1em}{}

% Table of contents styling
\renewcommand{\cftsecfont}{\sffamily\bfseries\color{dreamlab-purple}}
\renewcommand{\cftsubsecfont}{\sffamily\color{dreamlab-blue}}
\renewcommand{\cftsubsubsecfont}{\sffamily\color{dreamlab-grey}}

% Hyperref setup
\hypersetup{
    colorlinks=true,
    linkcolor=dreamlab-purple,
    citecolor=dreamlab-blue,
    urlcolor=dreamlab-lightblue,
    pdftitle={\@title},
    pdfauthor={DreamLab AI Consulting},
    bookmarks=true,
    bookmarksopen=true,
    bookmarksnumbered=true
}

% Custom commands
\newcommand{\companyname}{DreamLab AI Consulting}
\newcommand{\projectname}{AI Innovation Hub \& Holiday Retreat}

% Subtitle command
\newcommand{\subtitle}[1]{\def\@subtitle{#1}}
\def\@subtitle{}

% Financial formatting
\sisetup{
    group-separator={,},
    group-minimum-digits=3,
    detect-weight=true,
    detect-family=true
}
\newcommand{\gbp}[1]{£\num{#1}}
\newcommand{\euros}[1]{€\num{#1}}
\newcommand{\dollars}[1]{\$\num{#1}}

% Dual revenue stream commands
\newcommand{\trainingrevenue}[1]{\pounds{#1}\textsuperscript{T}}
\newcommand{\lettingrevenue}[1]{\pounds{#1}\textsuperscript{L}}
\newcommand{\totalrevenue}[1]{\pounds{#1}\textsuperscript{Total}}

% Custom environments for DreamLab
\newenvironment{keypoint}{%
    \begin{tcolorbox}[
        colback=dreamlab-lightgrey,
        colframe=dreamlab-purple,
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

% Training package commands
\newcommand{\packageduration}[1]{\textbf{Duration:} #1\par}
\newcommand{\packageprice}[1]{\textbf{Price:} #1\par}
\newcommand{\packagecapacity}[1]{\textbf{Capacity:} #1\par}
\newcommand{\packagedescription}[1]{\textit{#1}\par\vspace{0.5em}}
\newcommand{\packagemodules}[1]{\textbf{Modules:}\begin{itemize}#1\end{itemize}}

\newenvironment{trainingpackage}[1]{%
    \begin{tcolorbox}[
        colback=dreamlab-lightblue!10,
        colframe=dreamlab-blue,
        boxrule=1pt,
        arc=3mm,
        left=5mm,
        right=5mm,
        top=5mm,
        bottom=5mm,
        fonttitle=\bfseries\sffamily,
        title=#1
    ]
}{\end{tcolorbox}}

\newenvironment{lettinginfo}{%
    \begin{tcolorbox}[
        colback=dreamlab-green!10,
        colframe=dreamlab-green,
        boxrule=1pt,
        arc=3mm,
        left=5mm,
        right=5mm,
        top=5mm,
        bottom=5mm,
        fonttitle=\bfseries\sffamily,
        title=Holiday Let Information
    ]
}{\end{tcolorbox}}

\newenvironment{solarroi}{%
    \begin{tcolorbox}[
        colback=dreamlab-orange!10,
        colframe=dreamlab-orange,
        boxrule=1pt,
        arc=3mm,
        left=5mm,
        right=5mm,
        top=5mm,
        bottom=5mm,
        fonttitle=\bfseries\sffamily,
        title=Solar Investment ROI
    ]
}{\end{tcolorbox}}

% Solar system commands
\newcommand{\solarcost}[1]{\textbf{Investment:} #1\par}
\newcommand{\solarannualsavings}[1]{\textbf{Annual Savings:} #1\par}
\newcommand{\solarpayback}[1]{\textbf{Payback Period:} #1\par}
\newcommand{\solarnpv}[1]{\textbf{25-Year NPV:} #1\par}
\newcommand{\solarcarbonsaved}[1]{\textbf{CO2 Saved:} #1\par}

% Lab equipment specification environment
% Using a simpler table environment to avoid parsing issues
\newenvironment{labspec}{%
    \par\vspace{0.5em}
    \noindent\textbf{\sffamily Lab Equipment Specifications}\par\vspace{0.3em}
    \noindent\begin{tabular}{@{}p{3.5cm}p{7cm}rr@{}}
    \toprule
    \textbf{Equipment} & \textbf{Specifications} & \textbf{Quantity} & \textbf{Cost} \\
    \midrule
}{%
    \bottomrule
    \end{tabular}
    \par\vspace{0.5em}
}

% Availability calendar command
\newcommand{\availabilitycalendar}[2]{%
    \begin{tikzpicture}[every day/.style={anchor=center}]
        \calendar[
            dates=#1,
            day list downward,
            month label left,
            month text=\%mt \%y0,
            day xshift=3em,
            day letter headings
        ]
        if (Sunday) [red]
        #2;
    \end{tikzpicture}
}

% Title page command
\renewcommand{\maketitle}{%
    \begin{titlepage}
        \centering
        \vspace*{1cm}
        {\Huge\bfseries\sffamily\color{dreamlab-purple}\@title\par}
        \ifx\@subtitle\empty\else
            \vspace{0.5cm}
            {\Large\sffamily\color{dreamlab-dark}\@subtitle\par}
        \fi
        \vspace{1.5cm}

        \includegraphics[width=0.8\textwidth,height=0.4\textheight,keepaspectratio]{media/labview2.png}

        \vspace{1.5cm}

        {\Large\sffamily\@author\par}
        \vspace{1cm}
        {\large\sffamily\@date\par}
        \vfill

        \begin{tikzpicture}
            \node[rectangle,draw=dreamlab-purple,line width=2pt,minimum width=0.8\textwidth,minimum height=2.5cm,align=center] {
                \large\sffamily\companyname\\[0.5em]
                \normalsize\projectname\\[0.5em]
                \small\textit{Where AI Innovation Meets Sustainable Living}
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
        linecolor=dreamlab-purple,
        linewidth=1pt,
        backgroundcolor=dreamlab-lightgrey!20,
        skipabove=10pt,
        skipbelow=10pt,
        innertopmargin=10pt,
        innerbottommargin=10pt
    ]
}{\end{mdframed}}

% KPI display command with dual revenue streams
\newcommand{\dualrevenuekpi}[4]{%
    \begin{tikzpicture}
        \node[rectangle,draw=dreamlab-purple,fill=dreamlab-lightgrey,minimum width=3.5cm,minimum height=2.5cm,align=center] {
            {\small\sffamily #1}\\[0.3em]
            {\large\bfseries\sffamily Training: #2}\\[0.2em]
            {\large\bfseries\sffamily Letting: #3}\\[0.2em]
            {\footnotesize\sffamily #4}
        };
    \end{tikzpicture}
}

% Construction phase timeline
\newcommand{\phasedtimeline}[1]{%
    \begin{ganttchart}[
        hgrid,
        vgrid,
        bar/.style={fill=dreamlab-blue},
        group/.style={fill=dreamlab-purple},
        milestone/.style={fill=dreamlab-orange},
        link/.style={->,thick,dreamlab-green}
    ]{1}{12}
        #1
    \end{ganttchart}
}

% Cross-reference formatting
\crefname{section}{Section}{Sections}
\crefname{subsection}{Subsection}{Subsections}
\crefname{figure}{Figure}{Figures}
\crefname{table}{Table}{Tables}
\crefname{equation}{Equation}{Equations}

\endinput