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

### `$ hexonal stack`

```yaml
languages:  [Go, Rust, C#, C++, Python, Java, Ruby, TypeScript]
runtime:    [.NET, JVM, Node]
systems:    [Redis-protocol servers, storage engines, CLI tooling]
infra:      [Docker, Linux, Git]
currently:  [AI product infra, secure MCP tooling]
```

<br/>

### `$ hexonal contributions --merged`

<!-- MERGED:START -->
```diff
+ microsoft/garnet#2036  Fix out-of-bounds read in SCAN/HSCAN/SSCAN/ZSCAN when MATCH, COUNT or TYPE is the last token
+ microsoft/garnet#2037  Fix EXPIRE family double reply for incompatible options and session kill on braces in an option
+ microsoft/garnet#2041  Reject multiple source keys in BITOP NOT
```
<!-- MERGED:END -->

### `$ hexonal contributions --open`

<!-- OPEN:START -->
```diff
? microsoft/garnet#2050  Validate argument count in SET-family string commands
? microsoft/garnet#2040  Fix ZRANGESTORE aborting the RESP session on invalid range parameters
? microsoft/garnet#2038  Cap HRANDFIELD/ZRANDMEMBER count before packing it into arg1
? pmd/pmd#6885           [java] Fix CloneMethodMustImplementCloneable false positive for local-var throw
```
<!-- OPEN:END -->

<sub>found by reading the source, not just the issue tracker — root cause verified, regression-tested, adversarially reviewed before submitting.</sub>

<br/>

### `$ hexonal activity --graph`

<div align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=hexonal&theme=github-dark&hide_border=true&bg_color=00000000&color=39FF14&line=39FF14&point=39FF14&area=true&area_color=39FF14" width="100%"/>
</div>

<br/>

### `$ hexonal activity --snake`

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/hexonal/hexonal/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/hexonal/hexonal/output/github-contribution-grid-snake.svg" />
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/hexonal/hexonal/output/github-contribution-grid-snake-dark.svg" />
</picture>
</div>

<br/>

### `$ hexonal activity --streak`

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
