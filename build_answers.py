#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build 题目.json and 答案.json for FOFA competition package pkg-08e82c8d."""

import json
import os
import re
import zipfile

REF_DIR = "/Users/shiqingliang/Documents/Projects/temp/参考文档"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

PKG_ID = "pkg-08e82c8d"
PLAYER = "史庆亮"
FIXED = "该需求不能直接转换为FOFA搜索语句"


def load_questions():
    z = zipfile.ZipFile(os.path.join(REF_DIR, "题目.docx"))
    xml = z.read("word/document.xml").decode("utf-8")
    xml = xml.replace("</w:p>", "\n")
    txt = re.sub(r"<[^>]+>", "", xml)
    txt = (txt.replace("&quot;", '"').replace("&amp;", "&")
              .replace("&lt;", "<").replace("&gt;", ">"))
    return json.loads(txt.strip())


# id -> FOFA query (FIXED means "cannot be converted")
ANSWERS = {
    "M001-S009": 'ip="20.247.40.92"',
    "M002-S004": 'ip="124.255.254.0/24"',
    "M003-S002": 'domain="zendesk.com"',
    "M004-S003": 'host="www.amazon.com"',
    "M005-S004": 'domain="vpn"',
    "M006-S002": 'country="GB"',
    "M007-S007": 'country="KR" && region="Gangwon"',
    "M008-S009": 'country="DE" && region="Bavaria" && city="Munich"',
    "M009-S008": 'asn="4134"',
    "M010-S009": 'country="NL" && cloud_name="Amazon"',
    "M011-S005": 'region="Hebei" && cloud_name="Huawei"',
    "M012-S009": 'port="3000"',
    "M013-S003": '(title="Jenkins" || body="jenkins") && country!="CN" && after="2026-08-01"',
    "M014-S002": 'country="CN" && protocol="dns"',
    "M015-S001": FIXED,
    "M016-S006": 'protocol="ssh" && port="22022"',
    "M017-S001": 'protocol="tcp"',
    "M018-S006": 'protocol="snmp"',
    "M019-S010": 'country="US" && protocol="memcached"',
    "M020-S005": 'protocol="ftp"',
    "M021-S010": 'protocol="ssh" && banner="OpenSSH_10.4"',
    "M022-S007": 'country="JP" && app="Hikvision"',
    "M023-S002": 'domain="163.com" && host="~^[a-zA-Z0-9]\\.[a-zA-Z0-9]\\.163\\.com$"',
    "M024-S005": 'version="10.0.0"',
    "M025-S010": 'category="中间件"',
    "M026-S002": 'body="NoSuchUpload"',
    "M027-S008": 'header="Content-Security-Policy-Report-Only"',
    "M028-S011": 'status_code="308" && type="web"',
    "M029-S010": 'banner="SSH-2.0-OpenSSH_6.1"',
    "M030-S003": 'header="Set-Cookie:PHPSESSID"',
    "M031-S009": 'body="jquery.min.js"',
    "M032-S010": 'country="NL" && city="Amsterdam" && port="554" && banner="200 OK"',
    "M033-S003": 'cert.issuer.org="GlobalSign" && cert.is_expired=false',
    "M034-S007": 'cert.subject.cn="apple.com" && domain!="apple.com"',
    "M035-S010": 'cert="TrustAsia"',
    "M036-S007": 'cert.subject.org="Alibaba"',
    "M037-S008": 'domain="sohu.com" && banner!="" && banner!="apache"',
    "M038-S009": 'cert="adobe.com"',
    "M039-S001": 'cert.subject.cn="qq.com"',
    "M040-S011": 'cert="godaddy" && domain!="godaddy.com"',
    "M041-S001": 'cert="google.com" && is_honeypot=false && is_fraud=false',
    "M042-S003": 'cert.subject.cn="example.com" || cert.domain="example.com"',
    "M043-S004": 'tls.version="TLS 1.0" && cert.is_expired=false',
    "M044-S007": 'jarm="21d21d00021d21d00021d21d21d21dce319294781f0e12867fd06896a000ea" && status_code="307" && header="Content-Length: 0"',
    "M045-S001": 'os="linux"',
    "M046-S013": 'country="CN" && is_domain=false && type="web"',
    "M047-S011": 'cert.is_match=false',
    "M048-S001": 'country="CA" && cert.is_match=false',
    "M049-S010": 'country="TR" && ja3s="f4febc55ea12b31ae17cfb7e614afda8"',
    "M050-S004": 'org="Inc"',
    "M051-S001": 'country="US" && org="OVH SAS" && port="2087" && title=="WHM 登录"',
    "M052-S002": 'domain=".io" && app="WordPress"',
    "M053-S009": 'city="Xiamen" && port="80" && status_code="200"',
    "M054-S009": 'country="GB" && cloud_name="DigitalOcean" && body="/api/show"',
    "M055-S003": 'country="CN" && header="Set-Cookie" && body="/admin"',
    "M056-S008": 'domain="baidu.com" && (body="Login" || body="admin" || body="Dashboard" || body="管理" || header="Set-Cookie")',
    "M057-S012": 'ip="13.0.0.0/8" && status_code="200" && (body="Welcome" || body="Sign in" || body="Dashboard")',
    "M058-S012": 'country="DE" && (host="amazonaws.com" || domain="amazonaws.com" || cname="amazonaws.com" || cert="amazonaws.com" || cert.domain="amazonaws.com")',
    "M059-S006": 'port="143" && cert.serial_number="1" && (cert="TAK" || cert="ATAK" || cert="WinTAK" || cert="Squad" || cert="CoT")',
    "M060-S010": 'ip="113.247.228.0/24" && (port="80" || port="443" || port="8080" || port="8443")',
    "M061-S005": '(title="Sign in" || title="Login") && port="80" && is_ipv6=false',
    "M062-S010": 'country="NZ" && (port="80" || port="443") && cloud_name!=""',
    "M063-S001": '(banner="IIS" && banner="1.") || header="IIS"',
    "M064-S004": 'country="JP" && is_domain=true && port="443" && status_code="200" && cert.is_valid=true && (title="大学" || title="学部" || title="研究" || body="入学案内" || body="学生")',
    "M065-S004": 'domain="baidu.com" && (title="系统" || title="平台" || title="登录" || title="管理" || title="API" || host="api" || host="admin" || host="dev" || host="test" || host="uat" || host="pre")',
    "M066-S006": 'category="邮件系统" && title="Mail" && country!="US"',
    "M067-S008": 'country="CN" && port="8888"',
    "M068-S005": 'body="Jenkins" && title!="Jenkins"',
    "M069-S001": 'country="TW" && asn="20940" && port="443" && tls.version="TLS 1.3" && cert.issuer.org!="Let\'s Encrypt" && cert.issuer.org!="ZeroSSL"',
    "M070-S003": 'app="HFS" && status_code="200" && title=="HFS /" && country!="JP" && cloud_name!="Amazon"',
    "M071-S006": 'country="CN" && app="Grafana"',
    "M072-S008": 'domain=".edu.ar" && (port="80" || port="443") && server!="Nginx" && app!="WAF"',
    "M073-S003": 'ip="1.1.1.1" && is_domain=true',
    "M074-S008": 'cert="aliyun.com" && cert.is_valid=true && is_domain=false',
    "M075-S006": 'country="CN" && is_domain=true && header="x-qiniu-zone" && domain!="qiniudn.com"',
    "M076-S004": 'title=="" && status_code="200" && fid!="" && icon_hash!="" && host="admin" && (domain=".cn" || domain="~^[a-zA-Z0-9]{4}\\.com$")',
    "M077-S009": 'body=\'class="container"\'',
    "M078-S009": 'body=\'"exception": "Symfony\\Component\\ErrorHandler\\Error\\FatalError"\'',
    "M079-S006": 'ip="40.88.0.0/16"',
    "M080-S006": '(ip="47.96.0.1" || ip="47.96.0.2" || ip="47.96.0.3" || ip="47.96.0.4" || ip="47.96.0.5") && (port="80" || port="443")',
    "M081-S011": 'app="Grafana" && ((header_hash!="" && body_hash!="") || (header_hash!="" && icon_hash!="") || (header_hash!="" && fid!="") || (body_hash!="" && icon_hash!="") || (body_hash!="" && fid!="") || (icon_hash!="" && fid!=""))',
    "M082-S001": '(domain="kuaihuoyun.com" || domain="wlhyos.cn" || domain="wlhyos.com" || domain="56ctms.com" || domain="xiaokuaikeji.com" || domain="zhihuiwuliu.org.cn" || cert.domain="kuaihuoyun.com" || cert.domain="wlhyos.cn" || cert.domain="wlhyos.com" || cert.domain="56ctms.com" || cert.domain="xiaokuaikeji.com" || cert.domain="zhihuiwuliu.org.cn") && cert.is_match=true && cert.is_valid=true',
    "M083-S008": 'header="Server: nginx" && title="Welcome"',
    "M084-S004": 'title="Grafana" && body="JavaScript"',
    "M085-S001": 'body="login" && (domain="bet" || domain="casino" || domain="kasino")',
    "M086-S006": 'domain="google" && domain!="google.com" && title==""',
    "M087-S009": 'header="server: Tengine" || header="x-cache: MISS"',
    "M088-S004": 'country="HK" && server=="Apache" && asn!="4134"',
    "M089-S010": 'app="HFS" && (port="80" || (port="8080" && status_code="200"))',
    "M090-S008": 'header="Content-Length: 1171" && header=\'Etag: "6aa522a3-493"\' && header="Accept-Ranges" && header="Cache-Control" && header="Content-Type" && header="Date" && header="Last-Modified" && header="Server" && header="Vary"',
    "M091-S009": FIXED,
    "M092-S007": FIXED,
    "M093-S004": FIXED,
    "M094-S004": FIXED,
    "M095-S010": FIXED,
    "M096-S001": 'body="Jenkins-Agent-Protocols" || body="Jenkins-Version" || body="Jenkins-Session"',
    "M097-S001": FIXED,
    "M098-S001": 'host="gov.cn."',
    "M099-S001": 'app="Apache HTTP Server"',
    "M100-S001": 'cert.issuer.cn="ZeroSSL ECC DV SSL CA 2" && cert.serial_number="63:BD:83:71:62:14:83:6E:F8:00:75:35:61:61:EB:06"',
}


def main():
    qs = load_questions()
    ids = [q["题号"] for q in qs]

    assert len(ids) == len(set(ids)) == 100, "question ids not 100 unique"
    missing = [i for i in ids if i not in ANSWERS]
    extra = [i for i in ANSWERS if i not in ids]
    assert not missing, f"missing answers: {missing}"
    assert not extra, f"unknown ids in answers: {extra}"

    with open(os.path.join(OUT_DIR, "题目.json"), "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    ans = {
        "选手名称": PLAYER,
        "参赛包编号": PKG_ID,
        "答案": [{"题号": i, "查询语句": ANSWERS[i]} for i in ids],
    }
    with open(os.path.join(OUT_DIR, "答案.json"), "w", encoding="utf-8") as f:
        json.dump(ans, f, ensure_ascii=False, indent=2)

    fixed = [i for i in ids if ANSWERS[i] == FIXED]
    print(f"questions: {len(ids)}  answers: {len(ans['答案'])}")
    print(f"cannot-convert ({len(fixed)}): {fixed}")
    print("wrote 题目.json and 答案.json")


if __name__ == "__main__":
    main()
