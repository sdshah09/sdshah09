<div align="center">

```
                    ╭────────────────────────╮
                 ╭──╯                        ╰──╮
                │                                │
                │    ●────────────────────●      │
                │                                │
                 ╰──╮                        ╭──╯
                    ╰────────────────────────╯
```

### Hello. I am **Shaswat**, your personal systems companion.

<sub>I was alerted to the need for medical attention when your p99 said *ow*.</sub>

<br>

<img src="https://img.shields.io/badge/✚%20SOFTWARE%20ENGINEER-E84A5F?style=for-the-badge&labelColor=E84A5F" alt="role"/>
<img src="https://img.shields.io/badge/CHICAGO,%20IL-FFFFFF?style=for-the-badge&labelColor=FFFFFF&color=2B2B2B" alt="location"/>
<img src="https://img.shields.io/badge/STATUS-ACTIVE%20CARE-FFFFFF?style=for-the-badge&labelColor=FFFFFF&color=2B2B2B" alt="status"/>

</div>

---

## ✚ &nbsp;Scan complete

```
SCANNING . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100%

  PATIENT      distributed systems, cloud infrastructure, LLM inference
  CLINICIAN    Shaswat Shah  ·  Software Engineer @ Curie
  SPECIALTY    healthcare platforms  ·  observability  ·  cost surgery
  LICENSE      M.S. Computer Engineering, Illinois Tech
```

**Diagnosis: your systems are in pain. Here is what I treated.**

| symptom | treatment administered | outcome |
|---|---|---|
| Cloud spend rising, nobody could say why | Custom Nginx-Go API gateway | **-40%** cost |
| GraphQL fanout inflating tail latency | Migrated the hot path to gRPC | **-70%** latency |
| Clinicians hand-building the same workflow | No-code React Flow engine | **-85%** time |
| Errors buried, triage by grep | Fluent Bit observability pipeline | **-93%** triage |
| Outages discovered by customers | Terraform SQS DLQ monitoring | **3h → 5min** |
| Claim prep taking analysts days | Azure Document Intelligence | **-85%** prep time |
| Extraction missing fields silently | RAG + hybrid search | **95%+** accuracy |

<sub>*I am programmed to report only measured outcomes. Each number above came from production, not a benchmark I designed to win.*</sub>

---

## ✚ &nbsp;Prescriptions

<sub>Dispensed publicly. Take as needed.</sub>

<table>
<tr><td width="50%" valign="top">

**[`amazon-design-doc`](https://github.com/sdshah09/design-doc-agent-skill)**

<a href="https://www.npmjs.com/package/amazon-design-doc"><img src="https://img.shields.io/npm/v/amazon-design-doc?style=flat-square&color=E84A5F&labelColor=FFFFFF&label=dose"/></a> <a href="https://www.npmjs.com/package/amazon-design-doc"><img src="https://img.shields.io/npm/dm/amazon-design-doc?style=flat-square&color=2B2B2B&labelColor=FFFFFF&label=dispensed%2Fmo"/></a>

```sh
npx amazon-design-doc install
```
*For teams whose design docs say "significantly faster" and never say why. Enforces the Amazon format across 7 agent runtimes.*

</td><td width="50%" valign="top">

**[`brag-document-skill`](https://github.com/sdshah09/brag-document-skill)**

<a href="https://www.npmjs.com/package/brag-document-skill"><img src="https://img.shields.io/npm/v/brag-document-skill?style=flat-square&color=E84A5F&labelColor=FFFFFF&label=dose"/></a> <a href="https://www.npmjs.com/package/brag-document-skill"><img src="https://img.shields.io/npm/dm/brag-document-skill?style=flat-square&color=2B2B2B&labelColor=FFFFFF&label=dispensed%2Fmo"/></a>

```sh
npx brag-document-skill
```
*For engineers who cannot remember what they shipped six months ago. Neither can their manager. This is treatable.*

</td></tr>
</table>

---

## ✚ &nbsp;Case files

<table>
<tr><td width="50%" valign="top">

### [SLOServe](https://github.com/sdshah09/sloserve)
`Python` · deadline-aware vLLM scheduling

> **Presenting complaint:** background batch jobs starve interactive requests on a shared GPU.
> **Approach:** deadline-aware scheduler, measured on deadline goodput at TTFT ≤ 500ms. Qwen3-8B on an L4, 80/20 mixed traffic, benchmarked against what vLLM already ships — FCFS, priority, chunked prefill.

</td><td width="50%" valign="top">

### [wispr](https://github.com/sdshah09/asr)
`Python` · Whisper, traced from zero

> **Presenting complaint:** everybody uses ASR, nobody can say what it does.
> **Approach:** traced the whole pipeline with real numbers. 11 scripts — mel spectrogram walkthrough, RTF benchmarks, quantization error on real weights, and a 10-case test set built specifically to make Whisper hallucinate.

</td></tr>
<tr><td width="50%" valign="top">

### [Distributed Message Broker](https://github.com/sdshah09/Distributed-Message-Broker-System)
`Python` · hypercube pub/sub

> **Vitals:** 1,861 RPS at 0.5ms. Failover in 8ms.
> Hypercube topology so no single node's loss partitions the mesh. Also [ported to C++](https://github.com/sdshah09/Distributed-Message-Broker-CPP).

</td><td width="50%" valign="top">

### [GoCore](https://github.com/sdshah09/GoCore)
`Go` · gRPC commerce services

> **Vitals:** account, product, and order services over gRPC with Elasticsearch, fully composed.
> A new developer is running the whole stack in 5 minutes.

</td></tr>
<tr><td width="50%" valign="top">

### [Real-time CDC Monitoring](https://github.com/sdshah09/Real-time-Database-Change-Monitoring-System)
`Python` · Postgres → Debezium → Kafka

> **Vitals:** row changes streamed the moment they commit.
> Zookeeper, broker, and connect all in one `docker-compose up`.

</td><td width="50%" valign="top">

### [Stock Prediction System](https://github.com/sdshah09/Stock-Prediction-and-Reporting-System)
`Python` · Django + ML forecasting

> **Vitals:** price forecasting with a custom reporting engine.
> Deployed to EC2 and RDS, shipped by GitHub Actions.

</td></tr>
</table>

<details>
<summary><b>&nbsp;✚&nbsp; Remaining charts</b> &nbsp;<sub>— 42 repositories on file</sub></summary>
<br>

| repository | condition treated | stack |
|---|---|---|
| [High-Throughput-Kafka-Messaging-Platform](https://github.com/sdshah09/High-Throughput-Kafka-Messaging-Platform) | Kafka tuned for throughput | `Go` |
| [Resilient-Hypercube-Framework](https://github.com/sdshah09/Resilient-Hypercube-Framework) | Fault-tolerant hypercube routing | `Python` |
| [P2P-Distributed-Message-Broker-System](https://github.com/sdshah09/P2P-Distributed-Message-Broker-System) | Async peer-to-peer pub/sub | `Python` |
| [KindConnect](https://github.com/jaygohel109/KindConnect) | WildHacks 2025 — MVP in under 24h, Gemini task routing | `FastAPI` |
| [OrderNotify-Bus](https://github.com/sdshah09/OrderNotify-Bus) | Event-driven microservices | `Java` |
| [Go-GraphQL](https://github.com/sdshah09/Go-GraphQL) · [gRPC-JS](https://github.com/sdshah09/gRPC-JS) | Protocol reference builds | `Go` `JS` |
| [Personal-Learner](https://github.com/sdshah09/Personal-Learner) | A personal learner to help you grow | `TypeScript` |
| [Design-Patterns](https://github.com/sdshah09/Design-Patterns) · [Neetcode-150](https://github.com/sdshah09/Neetcode-150) | GoF patterns, DSA | `Java` `Jupyter` |

</details>

---

## ✚ &nbsp;Treatment history

<details open>
<summary><b>Curie</b> &nbsp;·&nbsp; Software Engineer &nbsp;·&nbsp; <code>Feb 2025 — present</code> &nbsp;<sub>ongoing care</sub></summary>
<br>

```diff
+ Nginx-Go API gateway ................ cloud cost        -40%
+ GraphQL → gRPC migration ............ latency           -70%
+ No-code React Flow engine ........... clinical workflow -85%
+ Fluent Bit observability pipeline ... error triage      -93%
+ Terraform SQS DLQ monitoring ........ detection    3h → 5min
```

</details>

<details>
<summary><b>Briefed.IO</b> &nbsp;·&nbsp; Software Engineer &nbsp;·&nbsp; <code>Sep 2024 — Dec 2024</code> &nbsp;<sub>discharged</sub></summary>
<br>

```diff
+ Azure Document Intelligence ......... claim prep        -85%
+ Async ingestion pipeline ............ infra cost        -70%
+ RAG + hybrid search ................. accuracy        95%+
+ HIPAA-compliant MVP ................. React / Postgres
```

</details>

<details>
<summary><b>Dosepack LLP</b> &nbsp;·&nbsp; Software Engineer &nbsp;·&nbsp; <code>May 2022 — Jun 2023</code> &nbsp;<sub>discharged</sub></summary>
<br>

```diff
+ Cloud-native Jenkins CI/CD .......... deploy time       -95%
+ AWS IoT Core (MQTT) ................. sync latency      -80%
+ Python FSM middleware ............... throughput        +20%
+ Git/Docker training program ......... onboarding        -66%
```

</details>

---

## ✚ &nbsp;Instruments

| | |
|---|---|
| **languages** | <img src="https://img.shields.io/badge/Go-FFFFFF?style=flat-square&logo=go&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Python-FFFFFF?style=flat-square&logo=python&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/TypeScript-FFFFFF?style=flat-square&logo=typescript&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/JavaScript-FFFFFF?style=flat-square&logo=javascript&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Java-FFFFFF?style=flat-square&logo=openjdk&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/C++-FFFFFF?style=flat-square&logo=cplusplus&logoColor=E84A5F&labelColor=FFFFFF"/> |
| **frameworks** | <img src="https://img.shields.io/badge/React-FFFFFF?style=flat-square&logo=react&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Next.js-FFFFFF?style=flat-square&logo=nextdotjs&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Node.js-FFFFFF?style=flat-square&logo=nodedotjs&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/FastAPI-FFFFFF?style=flat-square&logo=fastapi&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Django-FFFFFF?style=flat-square&logo=django&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/gRPC-FFFFFF?style=flat-square&logo=google&logoColor=E84A5F&labelColor=FFFFFF"/> |
| **infrastructure** | <img src="https://img.shields.io/badge/AWS-FFFFFF?style=flat-square&logo=amazonwebservices&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/GCP-FFFFFF?style=flat-square&logo=googlecloud&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Azure-FFFFFF?style=flat-square&logo=microsoftazure&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Kubernetes-FFFFFF?style=flat-square&logo=kubernetes&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Docker-FFFFFF?style=flat-square&logo=docker&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Terraform-FFFFFF?style=flat-square&logo=terraform&logoColor=E84A5F&labelColor=FFFFFF"/> |
| **data / streaming** | <img src="https://img.shields.io/badge/PostgreSQL-FFFFFF?style=flat-square&logo=postgresql&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Kafka-FFFFFF?style=flat-square&logo=apachekafka&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Debezium-FFFFFF?style=flat-square&logo=debezium&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Elasticsearch-FFFFFF?style=flat-square&logo=elasticsearch&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Redis-FFFFFF?style=flat-square&logo=redis&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/MongoDB-FFFFFF?style=flat-square&logo=mongodb&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/GraphQL-FFFFFF?style=flat-square&logo=graphql&logoColor=E84A5F&labelColor=FFFFFF"/> |
| **ml / inference** | <img src="https://img.shields.io/badge/PyTorch-FFFFFF?style=flat-square&logo=pytorch&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/vLLM-FFFFFF?style=flat-square&logoColor=E84A5F&labelColor=FFFFFF&color=2B2B2B"/> <img src="https://img.shields.io/badge/Whisper-FFFFFF?style=flat-square&logo=openai&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/HuggingFace-FFFFFF?style=flat-square&logo=huggingface&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/TensorFlow-FFFFFF?style=flat-square&logo=tensorflow&logoColor=E84A5F&labelColor=FFFFFF"/> |
| **devops / o11y** | <img src="https://img.shields.io/badge/GitHub_Actions-FFFFFF?style=flat-square&logo=githubactions&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Jenkins-FFFFFF?style=flat-square&logo=jenkins&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/CircleCI-FFFFFF?style=flat-square&logo=circleci&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/Fluent_Bit-FFFFFF?style=flat-square&logo=fluentbit&logoColor=E84A5F&labelColor=FFFFFF"/> <img src="https://img.shields.io/badge/OpenTelemetry-FFFFFF?style=flat-square&logo=opentelemetry&logoColor=E84A5F&labelColor=FFFFFF"/> |

---

## ✚ &nbsp;Credentials on file

```
  EDUCATION
  ─────────────────────────────────────────────────────────────────
  M.S. Computer Engineering    Illinois Institute of Technology
  GPA 3.8 / 4.0                Aug 2023 — May 2025

  B.E. Engineering             Gujarat Technological University
  GPA 3.6 / 4.0                Aug 2018 — May 2022

  CERTIFICATIONS
  ─────────────────────────────────────────────────────────────────
  ✚  AWS Cloud Practitioner (CLF-C02)
  ✚  Supervised ML: Regression & Classification — DeepLearning.AI
  ✚  Fundamentals of Deep Learning — NVIDIA
  ✚  Microsoft TEALS Volunteer
```

<details>
<summary><b>&nbsp;✚&nbsp; Verify this chart is authentic</b></summary>
<br>

```
PGP  0B9E F523 BDC6 F12E 3DC1  49F7 8D41 1137 2E48 E8E8
```

Full key and verification steps in [PGP.md](PGP.md).

</details>

---

## ✚ &nbsp;Vitals

<div align="center">

<img height="160em" src="https://github-readme-stats.vercel.app/api?username=sdshah09&show_icons=true&hide_border=true&bg_color=FFFFFF&title_color=E84A5F&text_color=2B2B2B&icon_color=E84A5F&include_all_commits=true&count_private=true"/>
<img height="160em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=sdshah09&layout=compact&hide_border=true&bg_color=FFFFFF&title_color=E84A5F&text_color=2B2B2B&langs_count=8"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sdshah09/sdshah09/main/dist/github-snake-dark.svg"/>
  <img alt="contribution activity" src="https://raw.githubusercontent.com/sdshah09/sdshah09/main/dist/github-snake.svg"/>
</picture>

</div>

---

<div align="center">

## On a scale of 1 to 10, how would you rate your pain?

```
      1        2        3        4        5        6        7        8        9       10
    ( ˘ ³˘)  ( ・∀・)  ( ˘_˘ )  ( ・_・)  ( ⚆_⚆ )  ( ≖_≖ )  ( >_< )  ( ×_× )  ( ಥ_ಥ )  ( ಠ益ಠ )

     ship     minor    flaky     p99      cloud     pager    silent    data     prod     it is
      it       bug      test    creep     bill      at 3am   failure   loss     down     friday
```

**Point to where it hurts. I cannot deactivate until you say you are satisfied with your care.**

<br>

<a href="mailto:shaswatshah2727@gmail.com"><img src="https://img.shields.io/badge/✚%20EMAIL-E84A5F?style=for-the-badge&labelColor=E84A5F" alt="Email"/></a>
<a href="https://linkedin.com/in/sdshah05"><img src="https://img.shields.io/badge/✚%20LINKEDIN-FFFFFF?style=for-the-badge&labelColor=FFFFFF&color=2B2B2B" alt="LinkedIn"/></a>
<a href="https://drive.google.com/file/d/1GdCquLV3BDOX2BF08x_KmwVTpnti63EI/view?usp=sharing"><img src="https://img.shields.io/badge/✚%20RESUME-FFFFFF?style=for-the-badge&labelColor=FFFFFF&color=2B2B2B" alt="Resume"/></a>

<br><br>

<sub>ba-la-la-la-la</sub>

<img src="https://komarev.com/ghpvc/?username=sdshah09&style=flat-square&color=E84A5F&labelColor=FFFFFF&label=patients%20seen" alt="views"/>

</div>
