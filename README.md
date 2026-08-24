<div align="center">

<img src="https://raw.githubusercontent.com/sdshah09/sdshah09/main/assets/sharingan.svg" width="600" alt="Hidden Leaf headband over a blinking Sharingan"/>

# 木ノ葉 &nbsp;·&nbsp; Shaswat Shah

**Jōnin, Distributed Systems Division** &nbsp;·&nbsp; Hidden Leaf Village of Chicago

<a href="https://linkedin.com/in/sdshah05"><img src="https://img.shields.io/badge/%E2%9C%A6%20Jonin-C1121F?style=for-the-badge&labelColor=C1121F" alt="✦ Jonin"/></a>
<img src="https://img.shields.io/badge/Village-Chicago%2C%20IL-1B2A41?style=flat-square&labelColor=1B2A41" alt="Village: Chicago, IL"/>
<img src="https://img.shields.io/badge/Status-Active%20duty-1B2A41?style=flat-square&labelColor=1B2A41" alt="Status: active duty"/>
<img src="https://img.shields.io/badge/Registration-009720-1B2A41?style=flat-square&labelColor=1B2A41" alt="Registration 009720"/>

</div>

---

## ⌁&nbsp; Mission log

<sub>Ranked by blast radius. Every result below was measured in production, not on a training ground.</sub>

| rank | mission | jutsu | result |
|:---:|:---|:---|---:|
| `S` | Cloud spend climbing, no owner | Custom Nginx-Go API gateway | **−40%** cost |
| `S` | Outages found by customers first | Terraform SQS DLQ monitoring | **3h → 5min** |
| `A` | GraphQL fanout inflating tail latency | Migrated hot path to gRPC | **−70%** latency |
| `A` | Triage by grep, errors buried | Fluent Bit observability pipeline | **−93%** triage |
| `A` | Clinicians rebuilding the same flow | No-code React Flow engine | **−85%** time |
| `A` | Claim prep costing analysts days | Azure Document Intelligence | **−85%** prep |
| `B` | Extraction dropping fields silently | RAG + hybrid search | **95%+** accuracy |
| `B` | Deploys slow enough to batch | Cloud-native Jenkins CI/CD | **−95%** deploy |
| `B` | Device sync lagging the floor | AWS IoT Core over MQTT | **−80%** latency |

---

## ⌁&nbsp; Sharingan — jutsu copied from other shinobi

<sub>Open source contributions. Status shown exactly as it stands; not every attempt lands.</sub>

| repository | reach | contribution | status |
|:---|---:|:---|:---|
| [entireio/cli](https://github.com/entireio/cli) | ★ 5.0k | [#2018](https://github.com/entireio/cli/pull/2018) spawn hooks via `node:child_process` for Desktop | **merged** |
| [entireio/cli](https://github.com/entireio/cli) | ★ 5.0k | [#1929](https://github.com/entireio/cli/pull/1929) sync imported checkpoints once logged in | in review |
| [entireio/cli](https://github.com/entireio/cli) | ★ 5.0k | [#1914](https://github.com/entireio/cli/pull/1914) qualify phone PII redaction as NANP-only | in review |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | ★ 30.7k | [#936](https://github.com/VoltAgent/awesome-agent-skills/pull/936) · [#935](https://github.com/VoltAgent/awesome-agent-skills/pull/935) list both published skills | in review |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | ★ 22.2k | [#1257](https://github.com/NVIDIA/NemoClaw/pull/1257) retry invalid custom policy preset selection | closed |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | ★ 22.2k | [#499](https://github.com/NVIDIA/NemoClaw/pull/499) document config, env overrides, my-stack | closed |
| [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | ★ 17.6k | [#1084](https://github.com/PrimeIntellect-ai/prime-agent/pull/1084) preserve MCP tool `inputSchema` from SDK snake_case | closed |

---

## ⌁&nbsp; Forbidden scrolls — published

<sub>Sealed, catalogued, and installable by anyone.</sub>

<table>
<tr><td width="50%" valign="top">

`S-rank` &nbsp; **[amazon-design-doc](https://github.com/sdshah09/design-doc-agent-skill)**

<a href="https://www.npmjs.com/package/amazon-design-doc"><img src="https://img.shields.io/npm/v/amazon-design-doc?style=flat-square&label=scroll&labelColor=1B2A41&color=C1121F"/></a> <a href="https://www.npmjs.com/package/amazon-design-doc"><img src="https://img.shields.io/npm/dm/amazon-design-doc?style=flat-square&label=copies%2Fmo&labelColor=1B2A41&color=94A3B8"/></a>

```sh
npx amazon-design-doc install
```

For teams whose design docs say *"significantly faster"* and never say why. Enforces the Amazon format across seven agent runtimes.

</td><td width="50%" valign="top">

`S-rank` &nbsp; **[brag-document-skill](https://github.com/sdshah09/brag-document-skill)**

<a href="https://www.npmjs.com/package/brag-document-skill"><img src="https://img.shields.io/npm/v/brag-document-skill?style=flat-square&label=scroll&labelColor=1B2A41&color=C1121F"/></a> <a href="https://www.npmjs.com/package/brag-document-skill"><img src="https://img.shields.io/npm/dm/brag-document-skill?style=flat-square&label=copies%2Fmo&labelColor=1B2A41&color=94A3B8"/></a>

```sh
npx brag-document-skill
```

For shinobi who cannot recall what they shipped six months ago. Neither can their captain. This is fixable.

</td></tr>
</table>

---

## ⌁&nbsp; Jutsu scrolls — built

<table>
<tr><td width="50%" valign="top">

`S-rank` &nbsp; **[SLOServe](https://github.com/sdshah09/sloserve)** · `Python`

Deadline-aware vLLM scheduling. Background batch work starves interactive requests on a shared GPU; this scores deadline goodput at TTFT ≤ 500ms, Qwen3-8B on an L4 under 80/20 mixed traffic — measured against what vLLM already ships, not a strawman.

</td><td width="50%" valign="top">

`A-rank` &nbsp; **[wispr](https://github.com/sdshah09/asr)** · `Python`

Whisper traced from zero with real numbers. Eleven scripts — mel spectrogram walkthrough, RTF benchmarks, quantization error on live weights, and a ten-case set built specifically to make the model hallucinate.

</td></tr>
<tr><td width="50%" valign="top">

`A-rank` &nbsp; **[Distributed Message Broker](https://github.com/sdshah09/Distributed-Message-Broker-System)** · `Python`

1,861 RPS at 0.5ms, failover in 8ms. Hypercube topology, so losing one node never partitions the mesh. Also [ported to C++](https://github.com/sdshah09/Distributed-Message-Broker-CPP).

</td><td width="50%" valign="top">

`B-rank` &nbsp; **[GoCore](https://github.com/sdshah09/GoCore)** · `Go`

Account, product, and order services over gRPC with Elasticsearch, fully composed. A new developer has the whole stack running in five minutes.

</td></tr>
<tr><td width="50%" valign="top">

`B-rank` &nbsp; **[Real-time CDC](https://github.com/sdshah09/Real-time-Database-Change-Monitoring-System)** · `Python`

Postgres row changes streamed the moment they commit — Debezium into Kafka, with Zookeeper, broker, and connect in one `docker-compose up`.

</td><td width="50%" valign="top">

`B-rank` &nbsp; **[Stock Prediction](https://github.com/sdshah09/Stock-Prediction-and-Reporting-System)** · `Python`

Django price forecasting with a custom reporting engine, deployed to EC2 and RDS, shipped by GitHub Actions.

</td></tr>
</table>

<details>
<summary><b>⌁&nbsp; Remaining scrolls</b> — <sub>42 repositories in the archive</sub></summary>
<br>

| scroll | technique | chakra |
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

## ⌁&nbsp; Rank progression

```
   ACADEMY    ├─ B.E. Engineering, Gujarat Technological University
   2018–2022  │  GPA 3.6 / 4.0

   GENIN      ├─ Dosepack LLP — Software Engineer
   2022–2023  │  CI/CD, AWS IoT Core, Python FSM middleware

   CHUNIN     ├─ M.S. Computer Engineering, Illinois Institute of Technology
   2023–2025  │  GPA 3.8 / 4.0
              ├─ Briefed.IO — Software Engineer
              │  Document intelligence, RAG, HIPAA-compliant MVP

   JONIN      ├─ Curie — Software Engineer
   2025–now   │  API gateway, gRPC migration, observability  ◀ current post
```

<details>
<summary><b>⌁&nbsp; Field certifications</b></summary>
<br>

```
  ✦  AWS Cloud Practitioner (CLF-C02)
  ✦  Supervised ML: Regression & Classification — DeepLearning.AI
  ✦  Fundamentals of Deep Learning — NVIDIA
  ✦  Microsoft TEALS Volunteer
```

</details>

<details>
<summary><b>⌁&nbsp; Verify this registration is authentic</b></summary>
<br>

```
PGP  0B9E F523 BDC6 F12E 3DC1  49F7 8D41 1137 2E48 E8E8
```

Full key and verification steps in [PGP.md](PGP.md).

</details>

---

## ⌁&nbsp; Chakra natures

| | |
|:---|:---|
| **ninjutsu — languages** | <img src="https://img.shields.io/badge/Go-1B2A41?style=flat-square&labelColor=1B2A41&logo=go&logoColor=E5E7EB" alt="Go"/> <img src="https://img.shields.io/badge/Python-1B2A41?style=flat-square&labelColor=1B2A41&logo=python&logoColor=E5E7EB" alt="Python"/> <img src="https://img.shields.io/badge/TypeScript-1B2A41?style=flat-square&labelColor=1B2A41&logo=typescript&logoColor=E5E7EB" alt="TypeScript"/> <img src="https://img.shields.io/badge/JavaScript-1B2A41?style=flat-square&labelColor=1B2A41&logo=javascript&logoColor=E5E7EB" alt="JavaScript"/> <img src="https://img.shields.io/badge/Java-1B2A41?style=flat-square&labelColor=1B2A41&logo=openjdk&logoColor=E5E7EB" alt="Java"/> <img src="https://img.shields.io/badge/C%2B%2B-1B2A41?style=flat-square&labelColor=1B2A41&logo=cplusplus&logoColor=E5E7EB" alt="C++"/> |
| **taijutsu — frameworks** | <img src="https://img.shields.io/badge/React-1B2A41?style=flat-square&labelColor=1B2A41&logo=react&logoColor=E5E7EB" alt="React"/> <img src="https://img.shields.io/badge/Next.js-1B2A41?style=flat-square&labelColor=1B2A41&logo=nextdotjs&logoColor=E5E7EB" alt="Next.js"/> <img src="https://img.shields.io/badge/Node.js-1B2A41?style=flat-square&labelColor=1B2A41&logo=nodedotjs&logoColor=E5E7EB" alt="Node.js"/> <img src="https://img.shields.io/badge/FastAPI-1B2A41?style=flat-square&labelColor=1B2A41&logo=fastapi&logoColor=E5E7EB" alt="FastAPI"/> <img src="https://img.shields.io/badge/Django-1B2A41?style=flat-square&labelColor=1B2A41&logo=django&logoColor=E5E7EB" alt="Django"/> <img src="https://img.shields.io/badge/gRPC-1B2A41?style=flat-square&labelColor=1B2A41" alt="gRPC"/> |
| **summoning — infrastructure** | <img src="https://img.shields.io/badge/AWS-1B2A41?style=flat-square&labelColor=1B2A41" alt="AWS"/> <img src="https://img.shields.io/badge/GCP-1B2A41?style=flat-square&labelColor=1B2A41&logo=googlecloud&logoColor=E5E7EB" alt="GCP"/> <img src="https://img.shields.io/badge/Azure-1B2A41?style=flat-square&labelColor=1B2A41" alt="Azure"/> <img src="https://img.shields.io/badge/Kubernetes-1B2A41?style=flat-square&labelColor=1B2A41&logo=kubernetes&logoColor=E5E7EB" alt="Kubernetes"/> <img src="https://img.shields.io/badge/Docker-1B2A41?style=flat-square&labelColor=1B2A41&logo=docker&logoColor=E5E7EB" alt="Docker"/> <img src="https://img.shields.io/badge/Terraform-1B2A41?style=flat-square&labelColor=1B2A41&logo=terraform&logoColor=E5E7EB" alt="Terraform"/> |
| **sealing — data & streaming** | <img src="https://img.shields.io/badge/PostgreSQL-1B2A41?style=flat-square&labelColor=1B2A41&logo=postgresql&logoColor=E5E7EB" alt="PostgreSQL"/> <img src="https://img.shields.io/badge/Kafka-1B2A41?style=flat-square&labelColor=1B2A41&logo=apachekafka&logoColor=E5E7EB" alt="Kafka"/> <img src="https://img.shields.io/badge/Debezium-1B2A41?style=flat-square&labelColor=1B2A41" alt="Debezium"/> <img src="https://img.shields.io/badge/Elasticsearch-1B2A41?style=flat-square&labelColor=1B2A41&logo=elasticsearch&logoColor=E5E7EB" alt="Elasticsearch"/> <img src="https://img.shields.io/badge/Redis-1B2A41?style=flat-square&labelColor=1B2A41&logo=redis&logoColor=E5E7EB" alt="Redis"/> <img src="https://img.shields.io/badge/MongoDB-1B2A41?style=flat-square&labelColor=1B2A41&logo=mongodb&logoColor=E5E7EB" alt="MongoDB"/> <img src="https://img.shields.io/badge/GraphQL-1B2A41?style=flat-square&labelColor=1B2A41&logo=graphql&logoColor=E5E7EB" alt="GraphQL"/> |
| **sage mode — ml & inference** | <img src="https://img.shields.io/badge/PyTorch-1B2A41?style=flat-square&labelColor=1B2A41&logo=pytorch&logoColor=E5E7EB" alt="PyTorch"/> <img src="https://img.shields.io/badge/vLLM-1B2A41?style=flat-square&labelColor=1B2A41" alt="vLLM"/> <img src="https://img.shields.io/badge/Whisper-1B2A41?style=flat-square&labelColor=1B2A41" alt="Whisper"/> <img src="https://img.shields.io/badge/HuggingFace-1B2A41?style=flat-square&labelColor=1B2A41&logo=huggingface&logoColor=E5E7EB" alt="HuggingFace"/> <img src="https://img.shields.io/badge/TensorFlow-1B2A41?style=flat-square&labelColor=1B2A41&logo=tensorflow&logoColor=E5E7EB" alt="TensorFlow"/> |
| **sensory — devops & o11y** | <img src="https://img.shields.io/badge/GitHub_Actions-1B2A41?style=flat-square&labelColor=1B2A41&logo=githubactions&logoColor=E5E7EB" alt="GitHub Actions"/> <img src="https://img.shields.io/badge/Jenkins-1B2A41?style=flat-square&labelColor=1B2A41&logo=jenkins&logoColor=E5E7EB" alt="Jenkins"/> <img src="https://img.shields.io/badge/CircleCI-1B2A41?style=flat-square&labelColor=1B2A41&logo=circleci&logoColor=E5E7EB" alt="CircleCI"/> <img src="https://img.shields.io/badge/Fluent_Bit-1B2A41?style=flat-square&labelColor=1B2A41&logo=fluentbit&logoColor=E5E7EB" alt="Fluent Bit"/> <img src="https://img.shields.io/badge/OpenTelemetry-1B2A41?style=flat-square&labelColor=1B2A41&logo=opentelemetry&logoColor=E5E7EB" alt="OpenTelemetry"/> <img src="https://img.shields.io/badge/Argo_CD-1B2A41?style=flat-square&labelColor=1B2A41&logo=argo&logoColor=E5E7EB" alt="Argo CD"/> <img src="https://img.shields.io/badge/Sentry-1B2A41?style=flat-square&labelColor=1B2A41&logo=sentry&logoColor=E5E7EB" alt="Sentry"/> |

---

## ⌁&nbsp; Chakra output

<!-- chakra:start -->
```
CHAKRA DISTRIBUTION   42 repositories, by primary language

  Python            ██████████████████████████████████ 17
  JavaScript        ██████████████                      7
  Go                ████████                            4
  Java              ████████                            4
  Jupyter Notebook  ████████                            4
  C++               ██                                  1
  TypeScript        ██                                  1
```
<!-- chakra:end -->

<sub>Counted by repository, not by bytes — notebook outputs and vendored build files are stored base64 and would otherwise drown out everything actually written. Regenerated daily by <a href="scripts/chakra.py">scripts/chakra.py</a>.</sub>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sdshah09/sdshah09/main/dist/github-snake-dark.svg"/>
  <img alt="contribution activity" src="https://raw.githubusercontent.com/sdshah09/sdshah09/main/dist/github-snake.svg"/>
</picture>

</div>

---

<div align="center">

### ⌁&nbsp; Summon

<a href="mailto:shaswatshah2727@gmail.com"><img src="https://img.shields.io/badge/Email-C1121F?style=for-the-badge&labelColor=C1121F&logo=gmail&logoColor=E5E7EB" alt="Email"/></a>
<a href="https://linkedin.com/in/sdshah05"><img src="https://img.shields.io/badge/LinkedIn-1B2A41?style=for-the-badge&labelColor=1B2A41" alt="LinkedIn"/></a>
<a href="https://drive.google.com/file/d/1GdCquLV3BDOX2BF08x_KmwVTpnti63EI/view?usp=sharing"><img src="https://img.shields.io/badge/Resume-1B2A41?style=for-the-badge&labelColor=1B2A41&logo=googledrive&logoColor=E5E7EB" alt="Resume"/></a>

<br><br>

<!-- quote:start -->
<sub><i>&ldquo;People's lives don't end when they die. It ends when they lose faith.&rdquo;</i><br><br>&mdash; Itachi Uchiha</sub>
<!-- quote:end -->

<br>

<img src="https://komarev.com/ghpvc/?username=sdshah09&style=flat-square&label=scouted&labelColor=1B2A41&color=94A3B8" alt="visits"/>

</div>
