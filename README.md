<div align="center">

```
██╗  ██╗███████╗██╗  ██╗ ██████╗ ███╗   ██╗ █████╗ ██╗
██║  ██║██╔════╝╚██╗██╔╝██╔═══██╗████╗  ██║██╔══██╗██║
███████║█████╗   ╚███╔╝ ██║   ██║██╔██╗ ██║███████║██║
██╔══██║██╔══╝   ██╔██╗ ██║   ██║██║╚██╗██║██╔══██║██║
██║  ██║███████╗██╔╝ ██╗╚██████╔╝██║ ╚████║██║  ██║███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
```

<samp>root-causing bugs across storage engines, CLI tools &amp; RESP servers — verify before you trust a report, then verify your own fix</samp>

</div>

<br/>

```
┌─────────────────────────────────────────────────────────────┐
│ guest@hexonal ~ % whoami                                     │
├─────────────────────────────────────────────────────────────┤
│ name        hexonal                                          │
│ role        AI products / developer infra / MCP security     │
│ based_in    Chengdu, China                                   │
│ building    since 2018                                       │
│ right_now   root-causing bugs in garnet, kong, fmt, sinatra   │
│ motto       verify before you trust a report                 │
└─────────────────────────────────────────────────────────────┘
```

<p align="center">
  <a href="https://aipinmaker.com"><img src="https://img.shields.io/badge/site-aipinmaker.com-000000?style=flat-square&logo=googlechrome&logoColor=39FF14&labelColor=0d1117"/></a>
  <img src="https://img.shields.io/badge/location-成都-000000?style=flat-square&logo=googlemaps&logoColor=39FF14&labelColor=0d1117"/>
  <img src="https://img.shields.io/badge/org-Hexonal-000000?style=flat-square&logo=github&logoColor=39FF14&labelColor=0d1117"/>
  <img src="https://img.shields.io/badge/status-shipping-000000?style=flat-square&logo=git&logoColor=39FF14&labelColor=0d1117"/>
</p>

<br/>

### `$ cat stack.yml`

```yaml
languages:  [Go, Rust, C#, C++, Python, Java, Ruby, TypeScript]
runtime:    [.NET, JVM, Node]
systems:    [Redis-protocol servers, storage engines, CLI tooling]
infra:      [Docker, Linux, Git]
currently:  [AI product infra, secure MCP tooling]
```

<br/>

### `$ git log --oneline --merged`

```diff
+ fmtlib/fmt#4850      CMake export set generation
+ sinatra/sinatra#2182 commonmarker 2.9 CI breakage
+ microsoft/garnet#1937 PEM certificate support for TLS
```

### `$ git log --oneline --open`

```diff
? microsoft/garnet#1968  BITFIELD signed 64-bit overflow detection
? microsoft/garnet#1969  GETRANGE crash on empty-string values
? alecthomas/kong#629    flag/command validation ordering
? alecthomas/kong#630    nested camelCase config resolution
```

<sub>found by reading the source, not just the issue tracker — root cause verified, regression-tested, adversarially reviewed before submitting.</sub>

<br/>

### `$ ./activity --graph`

<div align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=hexonal&theme=github-dark&hide_border=true&bg_color=00000000&color=39FF14&line=39FF14&point=39FF14&area=true&area_color=39FF14" width="100%"/>
</div>

<br/>

### `$ ./contribution-snake.sh`

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/hexonal/hexonal/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/hexonal/hexonal/output/github-contribution-grid-snake.svg" />
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/hexonal/hexonal/output/github-contribution-grid-snake-dark.svg" />
</picture>
</div>

<br/>

<div align="center">
<img src="https://github-readme-streak-stats.herokuapp.com/?user=hexonal&theme=dark&hide_border=true&background=00000000&stroke=39FF14&ring=39FF14&fire=39FF14&currStreakLabel=39FF14&sideLabels=c9d1d9&currStreakNum=c9d1d9&sideNums=c9d1d9&dates=6e7681" />
</div>

<br/>

<div align="center">
<sub>

```
EOF 0
```

</sub>
</div>
