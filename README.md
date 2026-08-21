<div align="center">

```console
$ trace get --root shaswat.shah
```

```
TRACE 0b9ef523bdc6f12e    service: shaswat.shah    region: chicago-il    status: OK

├─ gtu.engineering    ···███████████████████······················   2018 ─ 2022
├─ dosepack.systems   ······················██████················   2022 ─ 2023
├─ illinoistech.msce  ····························█████████·······   2023 ─ 2025
├─ briefed.io         ··································██········   2024
└─ curie.engineering  ···································█████████   2025 ─ now  ⟵ active
                      ┴         ┴         ┴         ┴         ┴
                      2018      2020      2022      2024      2026
```

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=26&duration=3000&pause=1000&color=E84A5F&center=true&vCenter=true&multiline=true&repeat=true&width=680&height=90&lines=Software+Engineer;Distributed+Systems+%7C+Cloud+%7C+Inference;I+ship+things+and+then+I+measure+them" alt="Typing SVG" />

<a href="https://drive.google.com/file/d/1GdCquLV3BDOX2BF08x_KmwVTpnti63EI/view?usp=sharing"><img src="https://img.shields.io/badge/RESUME-E84A5F?style=for-the-badge&logoColor=white" alt="Resume"/></a>
<a href="mailto:shaswatshah2727@gmail.com"><img src="https://img.shields.io/badge/EMAIL-16213E?style=for-the-badge&logo=gmail&logoColor=E84A5F" alt="Email"/></a>
<a href="https://linkedin.com/in/sdshah05"><img src="https://img.shields.io/badge/LINKEDIN-16213E?style=for-the-badge&logo=linkedin&logoColor=4A90D9" alt="LinkedIn"/></a>
<a href="https://www.npmjs.com/~sdshah09"><img src="https://img.shields.io/badge/NPM-16213E?style=for-the-badge&logo=npm&logoColor=F8B500" alt="npm"/></a>

</div>

<br>

```console
$ shaswat --impact
```

<div align="center">

| `40%` | `70%` | `85%` | `93%` | `3h → 5min` |
|:---:|:---:|:---:|:---:|:---:|
| cloud cost cut | latency cut | faster clinical flows | faster error triage | outage detection |
| *Nginx-Go gateway* | *GraphQL → gRPC* | *no-code flow engine* | *Fluent Bit pipeline* | *Terraform SQS DLQ* |

</div>

---

## `$ ls -la ~/shipped`

> **42 repos.** Distributed systems, LLM inference, developer tooling, and two npm packages people can install today.

<table>
<tr>
<td width="50%" valign="top">

### 📦 [amazon-design-doc](https://github.com/sdshah09/design-doc-agent-skill)
<img src="https://img.shields.io/npm/v/amazon-design-doc?style=flat-square&color=E84A5F&labelColor=16213E" /> <img src="https://img.shields.io/npm/dm/amazon-design-doc?style=flat-square&color=F8B500&labelColor=16213E" />

```
├── npx amazon-design-doc install
├── Amazon-style design docs, enforced
├── 7 agent runtimes: Claude/Cursor/Codex/
│   Copilot/Windsurf/Gemini/AGENTS.md
└── JS · CI green · MIT
```

</td>
<td width="50%" valign="top">

### 📦 [brag-document-skill](https://github.com/sdshah09/brag-document-skill)
<img src="https://img.shields.io/npm/v/brag-document-skill?style=flat-square&color=E84A5F&labelColor=16213E" /> <img src="https://img.shields.io/npm/dm/brag-document-skill?style=flat-square&color=F8B500&labelColor=16213E" />

```
├── npx brag-document-skill
├── Turns your agent into a perf-review
│   record keeper (jvns.ca method)
├── Auto-detects installed tools
└── JS · 8 targets incl. Goose
```

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ⚡ [SLOServe](https://github.com/sdshah09/sloserve)
```
├── Deadline-aware vLLM scheduling
├── Metric: deadline goodput @ TTFT ≤500ms
├── Qwen3-8B on L4 · 80/20 mixed traffic
├── Baselines: FCFS, priority, chunked prefill
└── Python · mock server, no GPU needed
```

</td>
<td width="50%" valign="top">

### 🎙 [wispr — ASR from zero](https://github.com/sdshah09/asr)
```
├── Whisper traced end-to-end, real numbers
├── 11 scripts: mel trace, RTF bench,
│   quantization error, hallucination hunt
├── Adversarial 10-case failure test set
└── Python · dated reproducible reports
```

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🔀 [Distributed Message Broker](https://github.com/sdshah09/Distributed-Message-Broker-System)
```
├── 1,861 RPS @ 0.5ms latency
├── 8ms automatic failover
├── Hypercube pub/sub topology
└── Python + WebSockets · C++ port too
```

</td>
<td width="50%" valign="top">

### 🛒 [GoCore](https://github.com/sdshah09/GoCore)
```
├── Go + gRPC + Elasticsearch
├── Account / Product / Order services
├── Fully dockerized stack
└── 5 min developer onboarding
```

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📡 [Real-time CDC Monitoring](https://github.com/sdshah09/Real-time-Database-Change-Monitoring-System)
```
├── Postgres → Debezium → Kafka
├── Streams row changes as they happen
├── Zookeeper + broker + connect, composed
└── Python · one docker-compose up
```

</td>
<td width="50%" valign="top">

### 📈 [Stock Prediction System](https://github.com/sdshah09/Stock-Prediction-and-Reporting-System)
```
├── Django + ML price forecasting
├── Custom reporting engine
├── AWS EC2 + RDS deploy
└── CI/CD via GitHub Actions
```

</td>
</tr>
</table>

<details>
<summary><b>&nbsp;more from the shelf&nbsp;</b> · <sub>kafka, hackathons, event-driven demos, DSA</sub></summary>
<br>

| repo | what it is | stack |
|---|---|---|
| [High-Throughput-Kafka-Messaging-Platform](https://github.com/sdshah09/High-Throughput-Kafka-Messaging-Platform) | Kafka platform tuned for throughput | `Go` |
| [Resilient-Hypercube-Framework](https://github.com/sdshah09/Resilient-Hypercube-Framework) | Fault-tolerant hypercube routing | `Python` |
| [P2P-Distributed-Message-Broker-System](https://github.com/sdshah09/P2P-Distributed-Message-Broker-System) | Async P2P pub/sub | `Python` |
| [KindConnect](https://github.com/jaygohel109/KindConnect) | WildHacks 2025 — MVP in <24h, Gemini task routing | `FastAPI` |
| [OrderNotify-Bus](https://github.com/sdshah09/OrderNotify-Bus) | Event-driven microservices demo | `Java` |
| [Go-GraphQL](https://github.com/sdshah09/Go-GraphQL) · [gRPC-JS](https://github.com/sdshah09/gRPC-JS) | Protocol integration reference builds | `Go` `JS` |
| [Personal-Learner](https://github.com/sdshah09/Personal-Learner) | A personal learner to help you grow | `TypeScript` |
| [Design-Patterns](https://github.com/sdshah09/Design-Patterns) · [Neetcode-150](https://github.com/sdshah09/Neetcode-150) | GoF patterns + DSA grind | `Java` `Jupyter` |

</details>

---

## `$ cat tech_arsenal.md`

<div align="center">
<table>
<tr>
<td valign="top" width="33%">

### `languages`
<img src="https://img.shields.io/badge/Go-16213E?style=flat-square&logo=go&logoColor=E84A5F" alt="Go"/>
<img src="https://img.shields.io/badge/Python-16213E?style=flat-square&logo=python&logoColor=F8B500" alt="Python"/>
<img src="https://img.shields.io/badge/TypeScript-16213E?style=flat-square&logo=typescript&logoColor=4A90D9" alt="TypeScript"/>
<img src="https://img.shields.io/badge/JavaScript-16213E?style=flat-square&logo=javascript&logoColor=F8B500" alt="JavaScript"/>
<img src="https://img.shields.io/badge/Java-16213E?style=flat-square&logo=openjdk&logoColor=E84A5F" alt="Java"/>
<img src="https://img.shields.io/badge/C++-16213E?style=flat-square&logo=cplusplus&logoColor=4A90D9" alt="C++"/>

</td>
<td valign="top" width="33%">

### `frameworks`
<img src="https://img.shields.io/badge/React-16213E?style=flat-square&logo=react&logoColor=4A90D9" alt="React"/>
<img src="https://img.shields.io/badge/Next.js-16213E?style=flat-square&logo=nextdotjs&logoColor=EAEAEA" alt="Next.js"/>
<img src="https://img.shields.io/badge/Node.js-16213E?style=flat-square&logo=nodedotjs&logoColor=F8B500" alt="Node.js"/>
<img src="https://img.shields.io/badge/FastAPI-16213E?style=flat-square&logo=fastapi&logoColor=E84A5F" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Django-16213E?style=flat-square&logo=django&logoColor=F8B500" alt="Django"/>
<img src="https://img.shields.io/badge/gRPC-16213E?style=flat-square&logo=google&logoColor=4A90D9" alt="gRPC"/>

</td>
<td valign="top" width="33%">

### `infrastructure`
<img src="https://img.shields.io/badge/AWS-16213E?style=flat-square&logo=amazonwebservices&logoColor=F8B500" alt="AWS"/>
<img src="https://img.shields.io/badge/GCP-16213E?style=flat-square&logo=googlecloud&logoColor=E84A5F" alt="GCP"/>
<img src="https://img.shields.io/badge/Azure-16213E?style=flat-square&logo=microsoftazure&logoColor=4A90D9" alt="Azure"/>
<img src="https://img.shields.io/badge/Kubernetes-16213E?style=flat-square&logo=kubernetes&logoColor=4A90D9" alt="Kubernetes"/>
<img src="https://img.shields.io/badge/Docker-16213E?style=flat-square&logo=docker&logoColor=4A90D9" alt="Docker"/>
<img src="https://img.shields.io/badge/Terraform-16213E?style=flat-square&logo=terraform&logoColor=E84A5F" alt="Terraform"/>

</td>
</tr>
<tr>
<td valign="top" width="33%">

### `data / streaming`
<img src="https://img.shields.io/badge/PostgreSQL-16213E?style=flat-square&logo=postgresql&logoColor=4A90D9" alt="PostgreSQL"/>
<img src="https://img.shields.io/badge/Kafka-16213E?style=flat-square&logo=apachekafka&logoColor=EAEAEA" alt="Kafka"/>
<img src="https://img.shields.io/badge/Debezium-16213E?style=flat-square&logo=debezium&logoColor=E84A5F" alt="Debezium"/>
<img src="https://img.shields.io/badge/MongoDB-16213E?style=flat-square&logo=mongodb&logoColor=F8B500" alt="MongoDB"/>
<img src="https://img.shields.io/badge/Redis-16213E?style=flat-square&logo=redis&logoColor=E84A5F" alt="Redis"/>
<img src="https://img.shields.io/badge/Elasticsearch-16213E?style=flat-square&logo=elasticsearch&logoColor=F8B500" alt="Elasticsearch"/>
<img src="https://img.shields.io/badge/GraphQL-16213E?style=flat-square&logo=graphql&logoColor=E84A5F" alt="GraphQL"/>

</td>
<td valign="top" width="33%">

### `ml / inference`
<img src="https://img.shields.io/badge/PyTorch-16213E?style=flat-square&logo=pytorch&logoColor=E84A5F" alt="PyTorch"/>
<img src="https://img.shields.io/badge/vLLM-16213E?style=flat-square&logo=v&logoColor=4A90D9" alt="vLLM"/>
<img src="https://img.shields.io/badge/Whisper-16213E?style=flat-square&logo=openai&logoColor=EAEAEA" alt="Whisper"/>
<img src="https://img.shields.io/badge/HuggingFace-16213E?style=flat-square&logo=huggingface&logoColor=F8B500" alt="HuggingFace"/>
<img src="https://img.shields.io/badge/TensorFlow-16213E?style=flat-square&logo=tensorflow&logoColor=F8B500" alt="TensorFlow"/>

</td>
<td valign="top" width="33%">

### `devops / observability`
<img src="https://img.shields.io/badge/GitHub_Actions-16213E?style=flat-square&logo=githubactions&logoColor=EAEAEA" alt="GitHub Actions"/>
<img src="https://img.shields.io/badge/Jenkins-16213E?style=flat-square&logo=jenkins&logoColor=E84A5F" alt="Jenkins"/>
<img src="https://img.shields.io/badge/CircleCI-16213E?style=flat-square&logo=circleci&logoColor=F8B500" alt="CircleCI"/>
<img src="https://img.shields.io/badge/Fluent_Bit-16213E?style=flat-square&logo=fluentbit&logoColor=4A90D9" alt="Fluent Bit"/>
<img src="https://img.shields.io/badge/OpenTelemetry-16213E?style=flat-square&logo=opentelemetry&logoColor=F8B500" alt="OpenTelemetry"/>

</td>
</tr>
</table>
</div>

---

## `$ whoami`

```go
package main

type Engineer struct {
    Name      string
    Role      string
    Location  string
    Education string
    NowOn     []string
}

func main() {
    me := Engineer{
        Name:      "Shaswat Shah",
        Role:      "Software Engineer @ Curie",
        Location:  "Chicago, IL",
        Education: "M.S. Computer Engineering @ Illinois Tech",
        NowOn: []string{
            "LLM inference scheduling under SLOs",
            "Agent skills people actually npm-install",
            "Distributed systems that fail gracefully",
        },
    }
    _ = me // still compiling, like the rest of us
}
```

---

## `$ cat experience.log`

<details open>
<summary><b>Curie Remote</b> &nbsp;│&nbsp; Software Engineer &nbsp;│&nbsp; <code>Feb 2025 – Present</code></summary>
<br>

```diff
+ 40% cloud cost reduction      → Custom Nginx-Go API Gateway
+ 70% latency reduction         → GraphQL to gRPC migration
+ 85% faster clinical workflows → No-Code React Flow engine
+ 93% faster error triage       → Fluent Bit observability pipeline
+ 3h → 5min outage detection    → Terraform SQS DLQ monitoring
```

</details>

<details>
<summary><b>Briefed.IO</b> &nbsp;│&nbsp; Software Engineer &nbsp;│&nbsp; <code>Sep 2024 – Dec 2024</code></summary>
<br>

```diff
+ 85% reduced claim-prep time     → Azure Document Intelligence
+ 70% infrastructure cost cut     → Async ingestion pipeline
+ 95%+ extraction accuracy        → RAG + Hybrid Search
+ HIPAA-compliant MVP shipped     → React / PostgreSQL
```

</details>

<details>
<summary><b>Dosepack LLP</b> &nbsp;│&nbsp; Software Engineer &nbsp;│&nbsp; <code>May 2022 – Jun 2023</code></summary>
<br>

```diff
+ 95% faster deployments      → Cloud-Native Jenkins CI/CD
+ 80% reduced sync latency    → AWS IoT Core (MQTT)
+ 20% throughput increase     → Python FSM middleware
+ 66% faster onboarding       → Git/Docker training program
```

</details>

---

## `$ git stats --all`

<div align="center">
<img height="165em" src="https://github-readme-stats.vercel.app/api?username=sdshah09&show_icons=true&hide_border=true&bg_color=16213E&title_color=E84A5F&text_color=EAEAEA&icon_color=F8B500&include_all_commits=true&count_private=true"/>
<img height="165em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=sdshah09&layout=compact&hide_border=true&bg_color=16213E&title_color=E84A5F&text_color=EAEAEA&langs_count=8"/>
<br>
<img src="https://github-readme-streak-stats.herokuapp.com/?user=sdshah09&hide_border=true&background=16213E&stroke=4A90D9&ring=E84A5F&fire=F8B500&currStreakLabel=EAEAEA&sideLabels=EAEAEA&currStreakNum=E84A5F&sideNums=4A90D9&dates=EAEAEA" alt="streak"/>
<br>
<img alt="contribution snake" src="https://github.com/sdshah09/sdshah09/raw/output/github-snake-dark.svg"/>
</div>

---

## `$ cat credentials.txt`

```
┌──────────────────────────────────────────────────────────────────┐
│  EDUCATION                                                       │
├──────────────────────────────────────────────────────────────────┤
│  M.S. Computer Engineering   │ Illinois Institute of Technology  │
│  GPA 3.8/4.0                 │ Aug 2023 – May 2025               │
├──────────────────────────────────────────────────────────────────┤
│  B.E. Engineering            │ Gujarat Technological University  │
│  GPA 3.6/4.0                 │ Aug 2018 – May 2022               │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│  CERTIFICATIONS                                                  │
├──────────────────────────────────────────────────────────────────┤
│  ✓ AWS Cloud Practitioner (CLF-C02)                              │
│  ✓ Microsoft TEALS Volunteer                                     │
│  ✓ Supervised ML: Regression & Classification — DeepLearning.AI  │
│  ✓ Fundamentals of Deep Learning — NVIDIA                        │
└──────────────────────────────────────────────────────────────────┘
```

<details>
<summary><code>$ gpg --fingerprint</code></summary>
<br>

```
PGP: 0B9E F523 BDC6 F12E 3DC1 49F7 8D41 1137 2E48 E8E8
```

See [PGP.md](PGP.md) for the full key and verification steps.

</details>

---

<div align="center">

```
> connection established. say hi.
```

<a href="mailto:shaswatshah2727@gmail.com"><img src="https://img.shields.io/badge/-shaswatshah2727@gmail.com-E84A5F?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
<a href="https://linkedin.com/in/sdshah05"><img src="https://img.shields.io/badge/-sdshah05-4A90D9?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<img src="https://komarev.com/ghpvc/?username=sdshah09&style=flat-square&color=E84A5F&label=visitors" alt="views"/>

</div>
