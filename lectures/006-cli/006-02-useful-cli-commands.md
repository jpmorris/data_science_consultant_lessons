# `jq` (and aws)

## Get All EC2 Instance names

```bash
aws ec2 describe-instances --query 'Reservations[].Instances[].[InstanceId,InstanceType,PlatformDetails,(Tags[?Key==`Name`].Value)[0]]' |  jq -r '.[] | @csv'
```

## Get IP of machines by filter

```bash
 aws ec2 describe-instances  --filters "Name=tag:Name,Values=GAP-qa*" --query 'Reservations[].Instances[].[InstanceId,PrivateIpAddress,Tags[?Key==`Name`]| [0].Value] | sort_by(@, &[2])' --output text | tail -n 1 | awk -F" " '{print $2}'
```
