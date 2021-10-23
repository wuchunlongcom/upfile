# -*- coding: utf-8 -*-
#!/usr/bin/env bash
pushd `dirname $0` > /dev/null
BASE_DIR=`pwd -P`
popd > /dev/null

#############
# Functions
#############
function logging {
    echo "[INFO] $*"
}


#############
# Main
#############
cd ${BASE_DIR}
OPT_ENV_FORCE=$1


build_venv

# 初始化数据库。创建数据表,删除数据后再加载数据。谨慎操作！！！
if [ "${OPT_ENV_FORCE}x" == "-ix" ];then logging "i"; else logging "0";
fi

