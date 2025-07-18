# VNFap へのコントリビュート

VNFap は皆さんからのコントリビュートを歓迎します。ご協力いただける方のガイドラインは
以下の通りです:

## コントリビューション

VNFap またはその依存関係へのコントリビュートは、GitHub のプルリクエストの形で行ってください。
それぞれのプルリクエストは、コアコントリビューター（パッチの適用を許可されている人）によってレビューされ、
メインツリーに適用されるか、必要な変更についてのフィードバックが与えられます。
コアコントリビューターからのものであっても、すべてのコントリビューターはこのフォーマットに従うべきです。

ある issue に取り組みたい場合は、GitHub の issue にコメントすることで、まずその対応を主張してください。
これは、同じ issue に対するコントリビューターの重複作業を防ぐためです。

## プルリクエストのチェックリスト

- master ブランチからブランチし、必要であればプルリクエストを提出する前に現在の master ブランチにリベースしてください。
  master と正しくマージできない場合、変更をリベースするよう求められる可能性があります。

- コミットは、各コミットが独立して正しい（すなわち、各コミットがコンパイルされ、テストに合格する）ことを保証しながら、
  可能な限り小さくすべきです。

- コミットには、Developer Certificate of Origin (http://developercertificate.org) の sign-off を添えてください。
  これは、あなた（および該当する場合はあなたの雇用主）が [プロジェクトのライセンス](../LICENCE) の条項に拘束されることに
  同意していることを示すものです。git では、これは `git commit` の `-s` オプションを使います。

- もしあなたのパッチがレビューされなかったり、特定の人にレビューしてもらう必要がある場合、
  プルリクエストやコメントでレビューを依頼するレビュアーに@返信したり、[email](mailto:info@vnfap.com) でレビューを依頼することができます。

- 修正したバグや新機能に関連するテストを追加する。

具体的なgitの手順については、[GitHub workflow 101](https://github.com/servo/servo/wiki/GitHub-workflow)を参照してください。

## 行動規範

https://github.com/gitxstudent/vnfap/blob/master/docs/CODE_OF_CONDUCT.md

## コミュニケーション

