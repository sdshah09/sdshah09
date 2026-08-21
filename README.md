<div align="center">

```
  ╭────────────────────────────────────────╮  
╭─╯                                        ╰─╮
│                                            │
│    ●──────────────────────────────────●    │
│                                            │
╰─╮                                        ╭─╯
  ╰────────────────────────────────────────╯  
```

### Hello. I am **Shaswat**, your personal systems companion.

<sub>I was alerted to the need for medical attention when your p99 said <i>ow</i>.</sub>

<br>

<img src="https://img.shields.io/badge/%E2%9C%9A%20Software%20Engineer-D7263D?style=for-the-badge&labelColor=D7263D" alt="Software Engineer"/>
<img src="https://img.shields.io/badge/Chicago%2C%20IL-2B2D42?style=for-the-badge&labelColor=2B2D42" alt="Chicago, IL"/>
<img src="https://img.shields.io/badge/Status-Active%20care-D7263D?style=for-the-badge&labelColor=2B2D42&color=D7263D" alt="Status: active care"/>

</div>

---

## ✚&nbsp; Scan complete

```
SCANNING . . . . . . . . . . . . . . . . . . . . . . . . . .  100%

  PATIENT     distributed systems, cloud infra, LLM inference
  CLINICIAN   Shaswat Shah — Software Engineer @ Curie
  SPECIALTY   healthcare platforms, observability, cost surgery
  LICENSE     M.S. Computer Engineering, Illinois Tech
```

**Diagnosis: your systems are in pain. Here is what I treated.**

| symptom | treatment administered | outcome |
|:---|:---|---:|
| Cloud spend rising, nobody could say why | Custom Nginx-Go API gateway | **−40%** cost |
| GraphQL fanout inflating tail latency | Migrated the hot path to gRPC | **−70%** latency |
| Clinicians hand-building the same workflow | No-code React Flow engine | **−85%** time |
| Errors buried, triage by grep | Fluent Bit observability pipeline | **−93%** triage |
| Outages discovered by customers | Terraform SQS DLQ monitoring | **3h → 5min** |
| Claim prep taking analysts days | Azure Document Intelligence | **−85%** prep |
| Extraction dropping fields silently | RAG + hybrid search | **95%+** accuracy |

<sub><i>I am programmed to report measured outcomes only. Every number came from production, not from a benchmark designed to win.</i></sub>

---

## ✚&nbsp; Prescriptions

<table>
<tr><td width="50%" valign="top">

**[amazon-design-doc](https://github.com/sdshah09/design-doc-agent-skill)**

<a href="https://www.npmjs.com/package/amazon-design-doc"><img src="https://img.shields.io/npm/v/amazon-design-doc?style=flat-square&label=dose&labelColor=2B2D42&color=D7263D"/></a> <a href="https://www.npmjs.com/package/amazon-design-doc"><img src="https://img.shields.io/npm/dm/amazon-design-doc?style=flat-square&label=dispensed%2Fmo&labelColor=2B2D42&color=8D99AE"/></a>

```sh
npx amazon-design-doc install
```

For teams whose design docs say *"significantly faster"* and never say why. Enforces the Amazon format across 7 agent runtimes.

</td><td width="50%" valign="top">

**[brag-document-skill](https://github.com/sdshah09/brag-document-skill)**

<a href="https://www.npmjs.com/package/brag-document-skill"><img src="https://img.shields.io/npm/v/brag-document-skill?style=flat-square&label=dose&labelColor=2B2D42&color=D7263D"/></a> <a href="https://www.npmjs.com/package/brag-document-skill"><img src="https://img.shields.io/npm/dm/brag-document-skill?style=flat-square&label=dispensed%2Fmo&labelColor=2B2D42&color=8D99AE"/></a>

```sh
npx brag-document-skill
```

For engineers who cannot recall what they shipped six months ago. Neither can their manager. This is treatable.

</td></tr>
</table>

---

## ✚&nbsp; Case files

<table>
<tr><td width="50%" valign="top">

**[SLOServe](https://github.com/sdshah09/sloserve)** &nbsp;·&nbsp; `Python`

*Presenting complaint:* background batch jobs starve interactive requests on a shared GPU.

*Approach:* deadline-aware vLLM scheduler, scored on deadline goodput at TTFT ≤ 500ms. Qwen3-8B on an L4, 80/20 mixed traffic, measured against what vLLM already ships — FCFS, priority, chunked prefill.

</td><td width="50%" valign="top">

**[wispr](https://github.com/sdshah09/asr)** &nbsp;·&nbsp; `Python`

*Presenting complaint:* everyone uses ASR, nobody can say what it does.

*Approach:* traced the whole Whisper pipeline with real numbers. 11 scripts — mel spectrogram walkthrough, RTF benchmarks, quantization error on real weights, and a 10-case set built to make the model hallucinate.

</td></tr>
<tr><td width="50%" valign="top">

**[Distributed Message Broker](https://github.com/sdshah09/Distributed-Message-Broker-System)** &nbsp;·&nbsp; `Python`

*Vitals:* 1,861 RPS at 0.5ms. Failover in 8ms.

Hypercube topology, so losing one node never partitions the mesh. Also [ported to C++](https://github.com/sdshah09/Distributed-Message-Broker-CPP).

</td><td width="50%" valign="top">

**[GoCore](https://github.com/sdshah09/GoCore)** &nbsp;·&nbsp; `Go`

*Vitals:* account, product, and order services over gRPC with Elasticsearch.

Fully composed — a new developer has the stack running in 5 minutes.

</td></tr>
<tr><td width="50%" valign="top">

**[Real-time CDC Monitoring](https://github.com/sdshah09/Real-time-Database-Change-Monitoring-System)** &nbsp;·&nbsp; `Python`

*Vitals:* Postgres row changes streamed the moment they commit.

Debezium into Kafka; Zookeeper, broker, and connect in one `docker-compose up`.

</td><td width="50%" valign="top">

**[Stock Prediction System](https://github.com/sdshah09/Stock-Prediction-and-Reporting-System)** &nbsp;·&nbsp; `Python`

*Vitals:* Django price forecasting with a custom reporting engine.

Deployed to EC2 and RDS, shipped by GitHub Actions.

</td></tr>
</table>

<details>
<summary><b>✚&nbsp; Remaining charts</b> — <sub>42 repositories on file</sub></summary>
<br>

| repository | condition treated | stack |
|:---|:---|:---|
| [High-Throughput-Kafka-Messaging-Platform](https://github.com/sdshah09/High-Throughput-Kafka-Messaging-Platform) | Kafka tuned for throughput | `Go` |
| [Resilient-Hypercube-Framework](https://github.com/sdshah09/Resilient-Hypercube-Framework) | Fault-tolerant hypercube routing | `Python` |
| [P2P-Distributed-Message-Broker-System](https://github.com/sdshah09/P2P-Distributed-Message-Broker-System) | Async peer-to-peer pub/sub | `Python` |
| [KindConnect](https://github.com/jaygohel109/KindConnect) | WildHacks 2025 — MVP under 24h, Gemini task routing | `FastAPI` |
| [OrderNotify-Bus](https://github.com/sdshah09/OrderNotify-Bus) | Event-driven microservices | `Java` |
| [Go-GraphQL](https://github.com/sdshah09/Go-GraphQL) · [gRPC-JS](https://github.com/sdshah09/gRPC-JS) | Protocol reference builds | `Go` `JS` |
| [Personal-Learner](https://github.com/sdshah09/Personal-Learner) | A personal learner to help you grow | `TypeScript` |
| [Design-Patterns](https://github.com/sdshah09/Design-Patterns) · [Neetcode-150](https://github.com/sdshah09/Neetcode-150) | GoF patterns, DSA | `Java` `Jupyter` |

</details>

---

## ✚&nbsp; Treatment history

<details open>
<summary><b>Curie</b> · Software Engineer · <code>Feb 2025 — present</code> &nbsp;<sub>ongoing care</sub></summary>
<br>

```diff
+ Nginx-Go API gateway .............. cloud cost         -40%
+ GraphQL to gRPC migration ......... latency            -70%
+ No-code React Flow engine ......... clinical workflow  -85%
+ Fluent Bit observability .......... error triage       -93%
+ Terraform SQS DLQ monitoring ...... detection     3h to 5min
```

</details>

<details>
<summary><b>Briefed.IO</b> · Software Engineer · <code>Sep 2024 — Dec 2024</code> &nbsp;<sub>discharged</sub></summary>
<br>

```diff
+ Azure Document Intelligence ....... claim prep         -85%
+ Async ingestion pipeline .......... infra cost         -70%
+ RAG + hybrid search ............... accuracy          95%+
+ HIPAA-compliant MVP ............... React / Postgres
```

</details>

<details>
<summary><b>Dosepack LLP</b> · Software Engineer · <code>May 2022 — Jun 2023</code> &nbsp;<sub>discharged</sub></summary>
<br>

```diff
+ Cloud-native Jenkins CI/CD ........ deploy time        -95%
+ AWS IoT Core over MQTT ............ sync latency       -80%
+ Python FSM middleware ............. throughput         +20%
+ Git/Docker training program ....... onboarding         -66%
```

</details>

---

## ✚&nbsp; Instruments

| | |
|:---|:---|
| **languages** | <img src="https://img.shields.io/badge/Go-2B2D42?style=flat-square&labelColor=2B2D42&logo=go&logoColor=EDF2F4" alt="Go"/> <img src="https://img.shields.io/badge/Python-2B2D42?style=flat-square&labelColor=2B2D42&logo=python&logoColor=EDF2F4" alt="Python"/> <img src="https://img.shields.io/badge/TypeScript-2B2D42?style=flat-square&labelColor=2B2D42&logo=typescript&logoColor=EDF2F4" alt="TypeScript"/> <img src="https://img.shields.io/badge/JavaScript-2B2D42?style=flat-square&labelColor=2B2D42&logo=javascript&logoColor=EDF2F4" alt="JavaScript"/> <img src="https://img.shields.io/badge/Java-2B2D42?style=flat-square&labelColor=2B2D42&logo=openjdk&logoColor=EDF2F4" alt="Java"/> <img src="https://img.shields.io/badge/C%2B%2B-2B2D42?style=flat-square&labelColor=2B2D42&logo=cplusplus&logoColor=EDF2F4" alt="C++"/> |
| **frameworks** | <img src="https://img.shields.io/badge/React-2B2D42?style=flat-square&labelColor=2B2D42&logo=react&logoColor=EDF2F4" alt="React"/> <img src="https://img.shields.io/badge/Next.js-2B2D42?style=flat-square&labelColor=2B2D42&logo=nextdotjs&logoColor=EDF2F4" alt="Next.js"/> <img src="https://img.shields.io/badge/Node.js-2B2D42?style=flat-square&labelColor=2B2D42&logo=nodedotjs&logoColor=EDF2F4" alt="Node.js"/> <img src="https://img.shields.io/badge/FastAPI-2B2D42?style=flat-square&labelColor=2B2D42&logo=fastapi&logoColor=EDF2F4" alt="FastAPI"/> <img src="https://img.shields.io/badge/Django-2B2D42?style=flat-square&labelColor=2B2D42&logo=django&logoColor=EDF2F4" alt="Django"/> <img src="https://img.shields.io/badge/gRPC-2B2D42?style=flat-square&labelColor=2B2D42" alt="gRPC"/> |
| **infrastructure** | <img src="https://img.shields.io/badge/AWS-2B2D42?style=flat-square&labelColor=2B2D42" alt="AWS"/> <img src="https://img.shields.io/badge/GCP-2B2D42?style=flat-square&labelColor=2B2D42&logo=googlecloud&logoColor=EDF2F4" alt="GCP"/> <img src="https://img.shields.io/badge/Azure-2B2D42?style=flat-square&labelColor=2B2D42" alt="Azure"/> <img src="https://img.shields.io/badge/Kubernetes-2B2D42?style=flat-square&labelColor=2B2D42&logo=kubernetes&logoColor=EDF2F4" alt="Kubernetes"/> <img src="https://img.shields.io/badge/Docker-2B2D42?style=flat-square&labelColor=2B2D42&logo=docker&logoColor=EDF2F4" alt="Docker"/> <img src="https://img.shields.io/badge/Terraform-2B2D42?style=flat-square&labelColor=2B2D42&logo=terraform&logoColor=EDF2F4" alt="Terraform"/> |
| **data / streaming** | <img src="https://img.shields.io/badge/PostgreSQL-2B2D42?style=flat-square&labelColor=2B2D42&logo=postgresql&logoColor=EDF2F4" alt="PostgreSQL"/> <img src="https://img.shields.io/badge/Kafka-2B2D42?style=flat-square&labelColor=2B2D42&logo=apachekafka&logoColor=EDF2F4" alt="Kafka"/> <img src="https://img.shields.io/badge/Debezium-2B2D42?style=flat-square&labelColor=2B2D42" alt="Debezium"/> <img src="https://img.shields.io/badge/Elasticsearch-2B2D42?style=flat-square&labelColor=2B2D42&logo=elasticsearch&logoColor=EDF2F4" alt="Elasticsearch"/> <img src="https://img.shields.io/badge/Redis-2B2D42?style=flat-square&labelColor=2B2D42&logo=redis&logoColor=EDF2F4" alt="Redis"/> <img src="https://img.shields.io/badge/MongoDB-2B2D42?style=flat-square&labelColor=2B2D42&logo=mongodb&logoColor=EDF2F4" alt="MongoDB"/> <img src="https://img.shields.io/badge/GraphQL-2B2D42?style=flat-square&labelColor=2B2D42&logo=graphql&logoColor=EDF2F4" alt="GraphQL"/> |
| **ml / inference** | <img src="https://img.shields.io/badge/PyTorch-2B2D42?style=flat-square&labelColor=2B2D42&logo=pytorch&logoColor=EDF2F4" alt="PyTorch"/> <img src="https://img.shields.io/badge/vLLM-2B2D42?style=flat-square&labelColor=2B2D42" alt="vLLM"/> <img src="https://img.shields.io/badge/Whisper-2B2D42?style=flat-square&labelColor=2B2D42" alt="Whisper"/> <img src="https://img.shields.io/badge/HuggingFace-2B2D42?style=flat-square&labelColor=2B2D42&logo=huggingface&logoColor=EDF2F4" alt="HuggingFace"/> <img src="https://img.shields.io/badge/TensorFlow-2B2D42?style=flat-square&labelColor=2B2D42&logo=tensorflow&logoColor=EDF2F4" alt="TensorFlow"/> |
| **devops / o11y** | <img src="https://img.shields.io/badge/GitHub_Actions-2B2D42?style=flat-square&labelColor=2B2D42&logo=githubactions&logoColor=EDF2F4" alt="GitHub Actions"/> <img src="https://img.shields.io/badge/Jenkins-2B2D42?style=flat-square&labelColor=2B2D42&logo=jenkins&logoColor=EDF2F4" alt="Jenkins"/> <img src="https://img.shields.io/badge/CircleCI-2B2D42?style=flat-square&labelColor=2B2D42&logo=circleci&logoColor=EDF2F4" alt="CircleCI"/> <img src="https://img.shields.io/badge/Fluent_Bit-2B2D42?style=flat-square&labelColor=2B2D42&logo=fluentbit&logoColor=EDF2F4" alt="Fluent Bit"/> <img src="https://img.shields.io/badge/OpenTelemetry-2B2D42?style=flat-square&labelColor=2B2D42&logo=opentelemetry&logoColor=EDF2F4" alt="OpenTelemetry"/> |

---

## ✚&nbsp; Credentials on file

```
  EDUCATION
  ────────────────────────────────────────────────────────────────
  M.S. Computer Engineering     Illinois Institute of Technology
  GPA 3.8 / 4.0                 Aug 2023 — May 2025

  B.E. Engineering              Gujarat Technological University
  GPA 3.6 / 4.0                 Aug 2018 — May 2022

  CERTIFICATIONS
  ────────────────────────────────────────────────────────────────
  +  AWS Cloud Practitioner (CLF-C02)
  +  Supervised ML: Regression & Classification — DeepLearning.AI
  +  Fundamentals of Deep Learning — NVIDIA
  +  Microsoft TEALS Volunteer
```

<details>
<summary><b>✚&nbsp; Verify this chart is authentic</b></summary>
<br>

```
PGP  0B9E F523 BDC6 F12E 3DC1  49F7 8D41 1137 2E48 E8E8
```

Full key and verification steps in [PGP.md](PGP.md).

</details>

---

## ✚&nbsp; Vitals

<div align="center">

<img height="150em" src="https://github-readme-stats.vercel.app/api?username=sdshah09&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&bg_color=00000000&title_color=D7263D&text_color=8D99AE&icon_color=D7263D"/>
<img height="150em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=sdshah09&layout=compact&langs_count=8&hide_border=true&bg_color=00000000&title_color=D7263D&text_color=8D99AE&icon_color=D7263D"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sdshah09/sdshah09/main/dist/github-snake-dark.svg"/>
  <img alt="contribution activity" src="https://raw.githubusercontent.com/sdshah09/sdshah09/main/dist/github-snake.svg"/>
</picture>

</div>

---

<div align="center">

### On a scale of 1 to 10, how would you rate your pain?

```
   1      2      3      4      5      6      7      8      9      10
  \o/    :-)    :-|    :-/    :-(    >_<    x_x    @_@    T_T    RIP

  ship  minor  flaky   p99   cloud   3am   silent  data   prod  friday
   it    bug    test  creep   bill  pager   fail   loss   down  deploy
```

**Point to where it hurts.**
<br>
<sub>I cannot deactivate until you say you are satisfied with your care.</sub>

<br>

<a href="mailto:shaswatshah2727@gmail.com"><img src="https://img.shields.io/badge/Email-D7263D?style=for-the-badge&labelColor=D7263D&logo=gmail&logoColor=EDF2F4" alt="Email"/></a>
<a href="https://linkedin.com/in/sdshah05"><img src="https://img.shields.io/badge/LinkedIn-2B2D42?style=for-the-badge&labelColor=2B2D42" alt="LinkedIn"/></a>
<a href="https://drive.google.com/file/d/1GdCquLV3BDOX2BF08x_KmwVTpnti63EI/view?usp=sharing"><img src="https://img.shields.io/badge/Resume-2B2D42?style=for-the-badge&labelColor=2B2D42&logo=googledrive&logoColor=EDF2F4" alt="Resume"/></a>

<br><br>

<sub>ba-la-la-la-la</sub>

<img src="https://komarev.com/ghpvc/?username=sdshah09&style=flat-square&label=patients%20seen&labelColor=2B2D42&color=8D99AE" alt="visits"/>

</div>
