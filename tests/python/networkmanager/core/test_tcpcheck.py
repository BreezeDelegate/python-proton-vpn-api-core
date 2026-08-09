"""Tests for TCP reachability helpers."""
from unittest.mock import patch

import pytest

from proton.vpn.backend.networkmanager.core import tcpcheck


@pytest.mark.asyncio
async def test_is_any_port_reachable_checks_all_ports_until_one_succeeds():
    with patch.object(tcpcheck, "is_port_reachable", side_effect=[False, True]):
        assert await tcpcheck.is_any_port_reachable("127.0.0.1", [443, 8443]) is True


@pytest.mark.asyncio
async def test_is_any_port_reachable_returns_false_when_all_ports_fail():
    with patch.object(tcpcheck, "is_port_reachable", return_value=False):
        assert await tcpcheck.is_any_port_reachable("127.0.0.1", [443, 8443]) is False
