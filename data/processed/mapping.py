# file: map_region_ids.py
import pandas as pd
from typing import Dict, Iterable, Tuple
import argparse
import sys

# 1) 기본 매핑(질문에서 주신 값 그대로)
REGION_TO_ID: Dict[str, int] = {
    "경기": 1, "경남": 2, "충북": 3, "전북": 4, "인천": 5, "강원": 6,
    "경북": 7, "울산": 8, "충남": 9, "전남": 10, "부산": 11, "서울": 12,
    "대전": 13, "광주": 14, "대구": 15, "세종": 16, "제주": 17,
}

def add_region_id(
    df: pd.DataFrame,
    region_col: str = "region",
    new_col: str = "region_id",
    strict: bool = False
) -> Tuple[pd.DataFrame, Iterable[str]]:
    """
    df의 region_col을 REGION_TO_ID로 '정확히 일치' 매핑하여 new_col에 region_id 추가.
    strict=True면 매핑 실패 시 예외 발생.
    반환: (매핑된 DataFrame, 매핑 실패 지역 목록)
    """
    if region_col not in df.columns:
        raise KeyError(f"컬럼 '{region_col}' 이(가) CSV에 없습니다.")

    # 문자열 변환 및 양끝 공백 제거 정도만 수행 (정규화 없음)
    region_series = df[region_col].astype(str).map(lambda s: s.strip() if s is not None else s)

    df[new_col] = region_series.map(REGION_TO_ID)

    failed = sorted(set(region_series[df[new_col].isna()].dropna().astype(str)))

    if failed:
        msg = f"[경고] 매핑 실패 지역명(정확일치 필요): {failed}"
        if strict:
            raise ValueError(msg)
        else:
            print(msg, file=sys.stderr)

    return df, failed

def load_csv(path: str) -> pd.DataFrame:
    for enc in ("utf-8-sig", "utf-8", "cp949"):
        try:
            return pd.read_csv(path, encoding=enc)
        except UnicodeDecodeError:
            continue
    return pd.read_csv(path)

def save_csv(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False, encoding="utf-8-sig")

def main():
    parser = argparse.ArgumentParser(description="region → region_id 매핑 (정확일치)")
    parser.add_argument("input_csv", help="입력 CSV 경로 (region 컬럼 포함)")
    parser.add_argument("output_csv", help="결과 저장 CSV 경로")
    parser.add_argument("--region-col", default="region", help="지역명 컬럼명 (기본: region)")
    parser.add_argument("--new-col", default="region_id", help="생성할 지역ID 컬럼명 (기본: region_id)")
    parser.add_argument("--strict", action="store_true", help="매핑 실패 시 에러 발생")
    args = parser.parse_args()

    df = load_csv(args.input_csv)
    df, failed = add_region_id(df, region_col=args.region_col, new_col=args.new_col, strict=args.strict)
    save_csv(df, args.output_csv)

    if failed:
        print(f"저장 완료(경고 포함). 매핑 실패 {len(failed)}종: {failed}")
    else:
        print("저장 완료. 모든 지역이 정상 매핑되었습니다.")

if __name__ == "__main__":
    main()
