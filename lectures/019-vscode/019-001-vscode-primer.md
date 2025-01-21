# Visual Studio Code in CGAP Primer

# Sagemaker

Sagemaker includes many sub-services:

- Pipelines
- Studio
- Ground Truth
- Feature Store
- Experiments

# How to start a machine

- Select instance size medium for most work, scale up as needed, shut down large machines when not
  using, or small machines when you wont use them for a while
  - Still working on auto-shutdown--it's not very reliable
  - If you are using large libraries--like tensorflow--you should create a drive of 35Gig or greater
- To install the environment you need to select the Lifecycle Configuration for codeeditor-init
  - This configuration installs AWS CLI, UV (pip alternative), custom bashrc, creates ssh keys,
    installs extensions, adds hhs certificates to CA store, and syncs config files with s3 if they
    exist

# Post-install setup

- The first time you run a terminal it will prompt you to run the post-install script, and will keep
  prompting you until you do so.
- This script pulls most-used repos (text-analytics, grants-analytics-airflow, devops) gets EC2 ssh
  keys, modifies SAML aws token script to support 12 hour tokens (in dev)

# Python Environments

### Different Enviornments

#### The Distributions' python

Most distributions (the default Sagemaker images (we use these) use Ubuntu 22.04) package python as
part of the distribution to run various scripts and programs. However it's best to not modify the
distributions python as it make break some of these essential OS uses of python. There's essentially
no reason for us to use it.

#### Anaconda python

The base python being used in sagemaker is from the scientific python package Anaconda. Install
packages using `conda`. But just don't use it, we will be using something better.

#### Base python

It is possible get/use python from python.org instead of using a packaged python and manager like
Anaconda. We don't need to do this. We essentially use the python packaged with Anaconda as our base
conda and use it to create virtual environments. The only thing we use from Anaconda is the base
python provided with Anaconda, nothing else. Everything else is fetched from Nexus.

### Virtual Environments

## UV cheat sheet

# Workflows

## Quickstart for code workflow

## Quickstart for Notebook workflow

## Quickstart for interactive workflow

# SQL Environments

You're better off using PgAdmin or DBeaver. There are notebook-based (Databricks style) SQL
workflows using certain plugins, but the plugins arn't very solid and the workflow may only make
sense for very long multi-step workflows (but we have Airflow)
