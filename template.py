"""
Generate activity tex files from section names.
"""
import re
import os

sections = ['Chain complexes',
'LES in homology',
'Chain homotopy',
'Mapping Cones and Cylinders',
'Resolutions',
'Derived functors',
'Categories, functors, and natural transformations',
'Adjunctions',
'Adjunctions and the Yoneda lemma',
'Adjunctions and exactness',
'Balancing Tor and Ext',
'Universal coefficient theorem',
'Homological dimension',
'Local rings, Koszul complexes',
'Gorenstein rings',
'Group cohomology',
'Local cohomology'
]


def make_template(name):
    """
    generate tex file name/name.tex using
    activity_boilerplate for tex code
    """
    activityName = camelize(name)
    os.system('mkdir -p ' + activityName)
    activityPath = activityName + '/' + activityName
    activityTex = activityPath + '.tex'
    print activityPath
    if not os.path.exists(activityTex):
        activityFile = open(activityTex,'w')
        activityFile.write(activity_boilerplate(name))
        activityFile.close()
    else:
        pass
        #print "tex file exists: " + activityTex

def make_many(names):
    for name in names:
        make_template(name)

def activity_boilerplate(name):
    """
    generate the tex code for activity
    """
    return r'''\documentclass{ximera}
\title{''' + name  + r'''}
\begin{document}
\begin{abstract}
% summary goes here

\end{abstract}
\maketitle

% content goes here

\end{document}
'''

def camelize(string, uppercase_first_letter=False, separator=' '):
    """
    Convert strings to camelBackCase.

    Based on
    https://github.com/jpvanhal/inflection/blob/master/inflection.py
    """
    s1 = re.sub('[^\s\w]','',string) #strip nonspace, nonword characters
    words = s1.split(separator)
    camelWords = [words[0].lower()] + [w.capitalize() for w in words[1:]]
    return ''.join(camelWords)
