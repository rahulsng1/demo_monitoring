from fabric.api import run, env, settings
from fabric.operations import sudo, local

env.hosts = open('hosts_file', 'r').readlines()
env.password = 'XXXXX'
def addduser():
        with settings(prompts={"Password: " : "XXXXX"}):
        run("sudo  userad testuser")
