# Site infrastructure — my-servers (moon Sol)

AWS hosting for this site lives in **`my-servers`**, not in this repo.

| Task | Path |
|------|------|
| Terraform | `~/Git/Machines/my-servers/moons/sol/terraform/` |
| Deploy | `~/Git/Machines/my-servers/moons/sol/deploy.sh` |
| Guide | `~/Git/Machines/my-servers/moons/sol/README.md` |
| Agent | `~/Git/Machines/my-servers/docs/agents/sol.md` |

This repo: **HTML/content** + [`.github/workflows/deploy.yml`](../.github/workflows/deploy.yml) (OIDC → S3 after `terraform apply` in my-servers).
